from collections import defaultdict
from typing import Sequence, Any

from src.models.student import StudentDTO
from .base import Reporter


class StudentPerformanceReporter(Reporter):

    report_key = "student-performance"

    def build_report(self, students_data: Sequence[StudentDTO]) -> list[dict[str, Any]]:
        student_grades: dict[str, list[int]] = defaultdict(lambda: [0, 0])  # sum and count of grades

        for student in students_data:
            student_grade = student_grades[student.student_name]
            student_grade[0] += student.grade
            student_grade[1] += 1

        report: list[dict[str, float]] = []

        student_avg_grades = ((name, total/count) for name, (total, count) in student_grades.items())

        sorted_student_avg_grades = sorted(student_avg_grades, key=lambda x: x[1], reverse=True)

        for i, (student, grade) in enumerate(sorted_student_avg_grades, start=1):
            report.append(
                {
                    "#": i,
                    "student_name": student,
                    "grade": grade
                }
            )

        return report



