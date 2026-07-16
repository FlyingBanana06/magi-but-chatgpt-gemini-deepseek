from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class SelectorLoader:
    """Load browser selectors from JSON files for each platform."""

    def __init__(self, base_dir: str | None = None):
        self.base_dir = Path(base_dir or Path(__file__).resolve().parent)

    def load(self, platform: str) -> dict[str, Any]:
        path = self.base_dir / f"{platform}.json"
        if not path.exists():
            return {
                "input": [],
                "submit": [],
                "response": [],
            }
        return json.loads(path.read_text(encoding="utf-8"))
