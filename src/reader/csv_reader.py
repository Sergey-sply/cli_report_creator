import csv
from datetime import date, datetime
from pathlib import Path
from typing import Sequence

from src.models.student import StudentDTO
from src.reader.base import BaseReader


class CSVReader(BaseReader):

    def read(self, paths: Sequence[str]) -> list[StudentDTO]:
            student_performance = []
            for path in paths:
                if not path.endswith(".csv"):
                    raise ValueError(f"Invalid file format: expected '<file>.csv', got '{path}'")
                try:
                    with open(path, "r", encoding="utf-8") as f:
                        reader = csv.DictReader(f)
                        for row in reader:
                            student_performance.append(
                                StudentDTO(
                                    student_name=row["student_name"].strip(),
                                    subject=row["subject"].strip(),
                                    teacher_name=row["teacher_name"].strip(),
                                    date=self._to_date(row["date"].strip()),
                                    grade=int(row["grade"].strip()),
                                )
                            )

                except FileNotFoundError as e:
                    raise FileNotFoundError(f"File not found: '{e.filename}'")

            return student_performance

    def _to_date(self, date_str: str) -> date:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        return date

