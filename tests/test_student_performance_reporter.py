import pytest
from datetime import date

from src.models.student import StudentDTO
from src.reporter import StudentPerformanceReporter, Reporter


def test_reporter_registry():
    r = Reporter.get("student-performance")
    assert isinstance(r, StudentPerformanceReporter)

def test_reporter_get_not_exist_reporter_key():
    with pytest.raises(ValueError) as e:
        Reporter.get("qwe-report")
    assert "does not exist" in str(e.value)

def test_student_performance_build_report():
    data = [
        StudentDTO("Алиса", "Математика", "Учитель 1", date(2024, 1, 1), 2),
        StudentDTO("Алиса", "Физика", "Учитель 2", date(2024, 1, 2), 3),
        StudentDTO("Петя", "Математика", "Учитель 1", date(2024, 1, 1), 4),
    ]
    r = StudentPerformanceReporter()
    report = r.build_report(data)

    # check report struct
    assert isinstance(report, list)
    assert report and {"#", "student_name", "grade"} <= set(report[0].keys())

    # check the order of elements
    names = [row["student_name"] for row in report]
    assert set(names) == {"Петя", "Алиса"}

    # check calculated avg grades
    grades = {row["student_name"]: row["grade"] for row in report}
    assert grades["Алиса"] == pytest.approx(2.5)
    assert grades["Петя"] == pytest.approx(4.0)
