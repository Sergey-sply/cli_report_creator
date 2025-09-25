from dataclasses import dataclass
from datetime import date


@dataclass(frozen=True, slots=True)
class StudentDTO:
    student_name: str
    subject: str
    teacher_name: str
    date: date
    grade: int
