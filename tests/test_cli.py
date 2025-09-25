from cli import main

def test_cli_ok_prints(tmp_path, csv_data, capsys):
    p = tmp_path / "tmp_students.csv"
    p.write_text(csv_data, encoding="utf-8")

    main(["--files", str(p), "--report", "student-performance"])
    out = capsys.readouterr().out

    assert "student_name" in out
    assert "Алиса" in out

def test_cli_empty_file_warn_print(tmp_path, csv_empty, capsys):
    p = tmp_path / "empty.csv"
    p.write_text(csv_empty, encoding="utf-8")

    main(["--files", str(p), "--report", "student-performance"])
    out = capsys.readouterr().out

    assert "[WARNING] No data in files" in out

def test_cli_not_exist_reporter_key_print(tmp_path, csv_data, capsys):
    p = tmp_path / "tmp_students.csv"
    p.write_text(csv_data, encoding="utf-8")

    main(["--files", str(p), "--report", "no-such-report"])
    out = capsys.readouterr().out

    assert "[ERROR]" in out
    assert "does not exist" in out
