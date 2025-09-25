import textwrap
import pytest

@pytest.fixture
def csv_data():
    return textwrap.dedent("""\
        student_name,subject,teacher_name,date,grade
        Алииса,Математика,Учитель 1,2024-01-01,2
        Петя,Математика,Учитель 1,2024-01-02,3
        Алиса,Физика,Учитель 2,2024-01-03,4
    """)

@pytest.fixture
def csv_empty():
    return "student_name,subject,teacher_name,date,grade"
