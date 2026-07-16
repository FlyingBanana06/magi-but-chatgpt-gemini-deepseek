from __future__ import annotations

from magi.core.node import Persona
from .base import BaseProvider
from .chatgpt_browser import ChatGPTBrowserProvider
from .litellm_provider import LiteLLMProvider


def create_provider(kind: str = "litellm", *, model: str, persona: Persona, timeout: float = 60.0, **kwargs) -> BaseProvider:
    if kind == "litellm":
        return LiteLLMProvider(model=model, persona=persona, timeout=timeout)
    if kind in {"chatgpt-web", "chatgpt-browser"}:
        return ChatGPTBrowserProvider(headless=kwargs.get("headless", False), session_path=kwargs.get("session_path"))
    raise ValueError(f"Unsupported provider kind: {kind}")
