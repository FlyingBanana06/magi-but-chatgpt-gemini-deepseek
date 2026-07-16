from __future__ import annotations

import asyncio

import litellm

from magi.core.errors import AuthenticationError
from .base import BaseProvider


class LiteLLMProvider(BaseProvider):
    def __init__(self, model: str, persona, timeout: float = 60.0):
        self.model = model
        self.persona = persona
        self.timeout = timeout

    async def ask(self, prompt: str, *, system_prompt: str | None = None, timeout: float | None = None) -> str:
        effective_system_prompt = system_prompt or self.persona.system_prompt
        effective_timeout = timeout if timeout is not None else self.timeout
        try:
            response = await asyncio.wait_for(
                litellm.acompletion(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": effective_system_prompt},
                        {"role": "user", "content": prompt},
                    ],
                    num_retries=3,
                ),
                timeout=effective_timeout,
            )
            msg = response.choices[0].message
            content = msg.content
            if not content and hasattr(msg, "reasoning_content") and msg.reasoning_content:
                content = msg.reasoning_content
            if not content or not content.strip():
                raise ValueError("Provider returned empty response")
            return content.strip()
        except asyncio.TimeoutError as exc:
            raise TimeoutError(f"Provider timed out after {effective_timeout}s") from exc
        except litellm.AuthenticationError as exc:
            raise AuthenticationError(str(exc)) from exc
