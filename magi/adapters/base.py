from __future__ import annotations

from abc import ABC, abstractmethod


class BaseAdapter(ABC):
    """Adapter layer responsible for DOM-specific browser behavior."""

    @abstractmethod
    async def send_message(self, prompt: str) -> str:
        raise NotImplementedError
