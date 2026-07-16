from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class AuthManager:
    """Persist browser cookies and storage state for each platform."""

    def __init__(self, base_dir: str | None = None):
        self.base_dir = Path(base_dir or "sessions")
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def session_path(self, platform: str) -> Path:
        return self.base_dir / platform / "auth.json"

    async def save(self, context: Any, platform: str) -> Path:
        path = self.session_path(platform)
        path.parent.mkdir(parents=True, exist_ok=True)
        cookies = await context.cookies()
        path.write_text(json.dumps({"cookies": cookies}, indent=2), encoding="utf-8")
        return path

    async def load(self, context: Any, platform: str) -> bool:
        path = self.session_path(platform)
        if not path.exists():
            return False
        payload = json.loads(path.read_text(encoding="utf-8"))
        cookies = payload.get("cookies", [])
        if cookies:
            await context.add_cookies(cookies)
        return True
