import argparse
import asyncio
import json
from pathlib import Path

from playwright.async_api import async_playwright


async def save_session(platform: str) -> None:
    urls = {
        "chatgpt": "https://chatgpt.com",
        "gemini": "https://gemini.google.com",
        "deepseek": "https://chat.deepseek.com",
    }
    if platform not in urls:
        raise ValueError(f"Unsupported platform: {platform}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(urls[platform], wait_until="domcontentloaded")
        print(f"Please sign in to {platform} and then close the browser window.")
        while True:
            await asyncio.sleep(1)
            if page.is_closed():
                break

        cookies = await context.cookies()
        output_path = Path("sessions") / f"{platform}.json"
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(json.dumps({"cookies": cookies}, indent=2), encoding="utf-8")
        print(f"Saved session to {output_path}")
        await browser.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Save a browser session for MAGI")
    parser.add_argument("platform", choices=["chatgpt", "gemini", "deepseek"])
    args = parser.parse_args()
    asyncio.run(save_session(args.platform))
