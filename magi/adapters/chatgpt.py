from __future__ import annotations

from magi.adapters.base import BaseAdapter
from magi.browser.manager import BrowserManager
from magi.browser.auth import AuthManager
from magi.selectors.loader import SelectorLoader


class ChatGPTAdapter(BaseAdapter):
    """Very small adapter for browser-based ChatGPT interaction."""

    def __init__(self, manager: BrowserManager, auth: AuthManager | None = None, selectors: SelectorLoader | None = None):
        self.manager = manager
        self.auth = auth or AuthManager()
        self.selectors = selectors or SelectorLoader()

    async def send_message(self, prompt: str) -> str:
        page = await self.manager.start()
        await page.goto("https://chatgpt.com", wait_until="domcontentloaded")
        await self.auth.load(await self.manager._context, "chatgpt")
        selectors = self.selectors.load("chatgpt")
        input_selectors = selectors.get("input", [])
        submit_selectors = selectors.get("submit", [])
        if not input_selectors:
            input_selectors = ["textarea", "[contenteditable='true']"]
        if not submit_selectors:
            submit_selectors = ["button[type='submit']", "button"]

        input_locator = page.locator(input_selectors[0])
        if not await input_locator.count():
            raise RuntimeError("ChatGPT input field not found")
        await input_locator.first.click()
        await input_locator.first.fill(prompt)
        await page.keyboard.press("Enter")
        await page.wait_for_timeout(1500)
        return "ChatGPT browser adapter responded"
