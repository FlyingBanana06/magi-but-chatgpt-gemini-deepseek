import importlib
from unittest.mock import AsyncMock

import pytest

from magi.adapters.chatgpt import ChatGPTAdapter
from magi.browser.auth import AuthManager
from magi.browser.manager import BrowserManager
from magi.providers.chatgpt_browser import ChatGPTBrowserProvider
from magi.providers.factory import create_provider


def test_auth_manager_session_paths():
    auth = AuthManager(base_dir="/tmp/magi-test")
    assert auth.session_path("chatgpt").name == "auth.json"


def test_factory_creates_chatgpt_browser_provider():
    provider = create_provider("chatgpt-browser", model="ignored", persona=None, timeout=5.0)  # type: ignore[arg-type]
    assert provider.__class__.__name__ == "ChatGPTBrowserProvider"


def test_browser_manager_can_be_instantiated():
    manager = BrowserManager(headless=True)
    assert manager.page is None


def test_chatgpt_adapter_can_be_created():
    manager = BrowserManager(headless=True)
    adapter = ChatGPTAdapter(manager)
    assert adapter is not None


def test_chatgpt_browser_provider_can_be_created():
    provider = ChatGPTBrowserProvider(headless=True)
    assert provider.platform == "chatgpt"


def test_browser_provider_modules_import_without_cycle():
    modules = [
        "magi.providers.factory",
        "magi.providers.chatgpt_browser",
        "magi.providers.browser_base",
        "magi.providers.chatgpt_web",
        "magi.providers.litellm_provider",
        "magi.providers.base",
        "magi.adapters.chatgpt",
        "magi.adapters.base",
        "magi.browser.manager",
        "magi.browser.auth",
        "magi.selectors.loader",
        "magi.core.node",
    ]
    for module_name in modules:
        importlib.import_module(module_name)


@pytest.mark.asyncio
async def test_chatgpt_browser_provider_asks_with_mocked_adapter(monkeypatch):
    provider = ChatGPTBrowserProvider(headless=True)
    provider.initialize = AsyncMock()
    mocked_send = AsyncMock(return_value="mock response")
    provider.adapter.send_message = mocked_send

    result = await provider.ask("hello world")

    assert result == "mock response"
    mocked_send.assert_awaited_once_with("hello world")
