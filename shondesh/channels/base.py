from abc import ABC, abstractmethod
from typing import Dict, Any
import logging

from shondesh.formatters.base_formatter import Formatter

logger = logging.getLogger(__name__)


class Channel(ABC):
    """Abstract base class for channels"""

    def __init__(self, config: Dict, formatter: Formatter = None):
        self.config = config
        self.formatter = formatter

    @abstractmethod
    async def send(self, data: Any) -> bool:
        """Send alert for violation"""
        pass
