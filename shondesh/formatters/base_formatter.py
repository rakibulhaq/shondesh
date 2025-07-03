from abc import ABC, abstractmethod
from typing import Any


class Formatter(ABC):
    @abstractmethod
    def format(self, data) -> Any:
        pass
