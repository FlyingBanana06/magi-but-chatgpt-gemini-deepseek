from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from magi.providers.base import BaseProvider


class BrowserBaseProvider(BaseProvider):
    """Base class for browser-backed providers.

    This intentionally keeps the interface small: initialize a Playwright session,
    optionally load a persisted session file, and expose an async ask method.
    """

    def __init__(self, platform: str, *, headless: bool = False, session_path: str | None = None):
        self.platform = platform
        self.headless = headless
        self.session_path = session_path
        self._playwright = None
        self._browser = None
        self._context = None
        self._page = None

    async def initialize(self) -> None:
        from playwright.async_api import async_playwright

        self._playwright = await async_playwright().start()
        self._browser = await self._playwright.chromium.launch(headless=self.headless)
        self._context = await self._browser.new_context()
        self._page = await self._context.new_page()
        if self.session_path:
            await self._load_session(self.session_path)

    async def close(self) -> None:
        if self._context:
            await self._context.close()
        if self._browser:
            await self._browser.close()
        if self._playwright:
            await self._playwright.stop()

    async def _load_session(self, session_path: str) -> None:
        path = Path(session_path)
        if not path.exists():
            return
        with path.open("r", encoding="utf-8") as fh:
            payload = json.load(fh)
        cookies = payload.get("cookies", [])
        if cookies:
            await self._context.add_cookies(cookies)

    async def _save_session(self, session_path: str) -> None:
        path = Path(session_path)
        path.parent.mkdir(parents=True, exist_ok=True)
        cookies = await self._context.cookies()
        with path.open("w", encoding="utf-8") as fh:
            json.dump({"cookies": cookies}, fh, indent=2)

    async def ask(self, prompt: str, *, system_prompt: str | None = None, timeout: float | None = None) -> str:
        raise NotImplementedError
