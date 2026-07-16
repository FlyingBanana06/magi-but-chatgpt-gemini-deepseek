import pytest

from magi.core.node import MagiNode, MELCHIOR
from magi.providers.base import BaseProvider
from magi.providers.factory import create_provider


class StubProvider(BaseProvider):
    def __init__(self):
        self.calls = []

    async def ask(self, prompt: str, *, system_prompt: str | None = None, timeout: float | None = None) -> str:
        self.calls.append((prompt, system_prompt, timeout))
        return "stub response"


@pytest.mark.asyncio
async def test_magi_node_can_delegate_to_custom_provider():
    provider = StubProvider()
    node = MagiNode("melchior", "mock-model", MELCHIOR, provider=provider)

    result = await node.query("hello")

    assert result == "stub response"
    assert provider.calls[0][0] == "hello"
    assert provider.calls[0][1] == node.persona.system_prompt


def test_provider_factory_returns_litellm_provider():
    provider = create_provider("litellm", model="mock-model", persona=MELCHIOR, timeout=5.0)

    assert provider.__class__.__name__ == "LiteLLMProvider"
