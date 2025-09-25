from abc import ABC, abstractmethod
from typing import Sequence

from src.models.student import StudentDTO


class BaseReader(ABC):
    """
    base class for reading different file formats
    """

    @abstractmethod
    def read(self, paths: Sequence[str]) -> list[StudentDTO] | None: ...