from __future__ import annotations

from abc import ABC, abstractmethod


class BaseProvider(ABC):
    """Abstract interface for any MAGI backend provider."""

    @abstractmethod
    async def ask(self, prompt: str, *, system_prompt: str | None = None, timeout: float | None = None) -> str:
        """Send a prompt and return the provider's textual response."""
        raise NotImplementedError
