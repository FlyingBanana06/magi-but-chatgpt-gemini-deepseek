from dataclasses import dataclass
from typing import Optional

from magi.core.errors import AuthenticationError
from magi.providers.base import BaseProvider


@dataclass
class Persona:
    name: str
    description: str

    @property
    def system_prompt(self) -> str:
        return (
            f"You are {self.name}, one of the three MAGI decision nodes.\n"
            f"Your perspective: {self.description}\n"
            "Analyze the following query independently. Provide your honest assessment."
        )


# Built-in personas
MELCHIOR = Persona("Melchior", "You think like an analytical scientist. Prioritize logic, evidence, and precision.")
BALTHASAR = Persona("Balthasar", "You think like an empathetic caregiver. Prioritize human impact, safety, and ethical considerations.")
CASPER = Persona("Casper", "You think like a pragmatic realist. Prioritize feasibility, efficiency, and practical outcomes.")


class MagiNode:
    def __init__(
        self,
        name: str,
        model: str,
        persona: Persona,
        timeout: float = 60.0,
        provider: Optional[BaseProvider] = None,
    ):
        self.name = name
        self.model = model
        self.persona = persona
        self.timeout = timeout
        self.provider = provider
        if self.provider is None:
            from magi.providers.factory import create_provider
            self.provider = create_provider("litellm", model=model, persona=persona, timeout=timeout)

    async def query(self, prompt: str) -> str:
        """Send a query to this node's provider. Returns the response text or raises on failure."""
        try:
            return await self.provider.ask(prompt, system_prompt=self.persona.system_prompt, timeout=self.timeout)
        except TimeoutError:
            print(f"Node {self.name} ({self.model}) TIMEOUT after {self.timeout}s")
            raise TimeoutError(f"Node {self.name} ({self.model}) timed out after {self.timeout}s")
        except AuthenticationError as e:
            print(f"Node {self.name} ({self.model}) AUTH ERROR: {e}")
            raise AuthenticationError(
                f"Node {self.name} authentication failed. "
                f"Please set the API key for {self.model}. Error: {e}"
            ) from e
        except Exception as e:
            print(f"Node {self.name} ({self.model}) ERROR: {type(e).__name__}: {e}")
            raise e


