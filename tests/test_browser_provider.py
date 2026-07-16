import pytest

from magi.providers.browser_base import BrowserBaseProvider
from magi.providers.chatgpt_web import ChatGPTWebProvider


class DummyBrowserProvider(BrowserBaseProvider):
    async def ask(self, prompt: str, *, system_prompt: str | None = None, timeout: float | None = None) -> str:
        return "dummy"


def test_browser_provider_can_be_instantiated():
    provider = DummyBrowserProvider("chatgpt", headless=True)
    assert provider.platform == "chatgpt"


def test_chatgpt_web_provider_can_be_instantiated():
    provider = ChatGPTWebProvider(headless=True)
    assert provider.platform == "chatgpt"
