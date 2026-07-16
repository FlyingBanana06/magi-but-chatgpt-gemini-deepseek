from __future__ import annotations

from magi.adapters.chatgpt import ChatGPTAdapter
from magi.browser.auth import AuthManager
from magi.browser.manager import BrowserManager
from magi.providers.browser_base import BrowserBaseProvider


class ChatGPTBrowserProvider(BrowserBaseProvider):
    """Browser-based ChatGPT provider using the new adapter and browser infrastructure."""

    def __init__(self, *, headless: bool = False, session_path: str | None = None):
        super().__init__(platform="chatgpt", headless=headless, session_path=session_path)
        self.manager = BrowserManager(headless=headless)
        self.auth = AuthManager(base_dir=session_path or "sessions") if session_path else AuthManager()
        self.adapter = ChatGPTAdapter(self.manager, auth=self.auth)

    async def initialize(self) -> None:
        page = await self.manager.start()
        self._page = page
        self._context = self.manager._context
        self._browser = self.manager._browser
        self._playwright = self.manager._playwright

    async def ask(self, prompt: str, *, system_prompt: str | None = None, timeout: float | None = None) -> str:
        if self._page is None:
            await self.initialize()
        return await self.adapter.send_message(prompt)

    async def close(self) -> None:
        await self.manager.stop()
