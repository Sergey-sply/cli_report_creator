from abc import ABC, abstractmethod
from typing import Sequence, Any

from src.models.student import StudentDTO


class Reporter(ABC):
    """
    A collection of reporters

    Inherit this class, add report_key attribute
    and implement your class of Reporter
    """
    report_key: str

    _reporters = {}

    def __init_subclass__(cls):
        """
        This magical method, which is called every time a subclass is created
        """
        report_key = getattr(cls, "report_key", None)
        if report_key:
            Reporter._reporters[report_key] = cls

    @classmethod
    def get(cls, report_key: str, **kwargs) -> "Reporter":
        """
        Create a new instance of the class matching the specified key
        """
        reporter = cls._reporters.get(report_key)
        if not reporter:
            raise ValueError(f"Report '{report_key}' does not exist or is not registered")
        return reporter(**kwargs)

    @abstractmethod
    def build_report(self, students_data: Sequence[StudentDTO]) -> list[dict[str, Any]]:
        """
        Build list of rows for the report.

        Example return value:
            [
                {"Date": date(2025, 1, 1), "Teacher": "Maria",     "Grades": [5, 5, 2]},
                {"Date": date(2025, 1, 1), "Teacher": "Ekaterina", "Grades": [3, 5, 4]},
            ]
        """
        pass
