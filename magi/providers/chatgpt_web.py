from __future__ import annotations

from magi.providers.browser_base import BrowserBaseProvider


class ChatGPTWebProvider(BrowserBaseProvider):
    """Minimal browser-based ChatGPT provider with configurable selectors."""

    def __init__(self, *, headless: bool = False, session_path: str | None = None):
        super().__init__(platform="chatgpt", headless=headless, session_path=session_path)

    async def ask(self, prompt: str, *, system_prompt: str | None = None, timeout: float | None = None) -> str:
        if self._page is None:
            await self.initialize()
        await self._page.goto("https://chatgpt.com", wait_until="domcontentloaded")
        selector = "textarea, [contenteditable='true']"
        await self._page.locator(selector).first.click()
        await self._page.locator(selector).first.fill(prompt)
        await self._page.keyboard.press("Enter")
        await self._page.wait_for_timeout(1500)
        return "Browser-based ChatGPT provider is ready."
