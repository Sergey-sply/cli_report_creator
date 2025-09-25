import pytest

from src.models.student import StudentDTO
from src.reader.csv_reader import CSVReader


def test_csv_reader_single_file(tmp_path, csv_data):
    file = tmp_path / "data.csv"
    file.write_text(csv_data, encoding="utf-8")

    reader = CSVReader()
    data = reader.read([str(file)])

    # check read data from csv
    assert isinstance(data, list)
    assert len(data) == 3
    assert isinstance(data[0], StudentDTO)

    # check data in dto
    assert data[0].grade == 2
    assert data[0].date.year == 2024

def test_csv_reader_invalid_file_format_raise(tmp_path, csv_data):
    file = tmp_path / "data.txt"
    file.write_text(csv_data, encoding="utf-8")

    reader = CSVReader()
    with pytest.raises(ValueError) as e:
        reader.read([str(file)])

    assert "Invalid file format" in str(e.value)

def test_csv_reader_file_not_found_raise():
    reader = CSVReader()
    with pytest.raises(FileNotFoundError) as e:
        reader.read(["not_exist.csv"])

    assert "File not found" in str(e.value)

def test_csv_reader_multiple_files(tmp_path, csv_data):
    file1 = tmp_path / "a.csv"
    file2 = tmp_path / "b.csv"
    file1.write_text(csv_data, encoding="utf-8")
    file2.write_text(csv_data, encoding="utf-8")

    reader = CSVReader()
    data = reader.read([str(file1), str(file2)])

    assert len(data) == 6
