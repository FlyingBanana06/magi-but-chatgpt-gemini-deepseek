# Provider layer

This package introduces a small abstraction layer for MAGI backends.

- BaseProvider defines the minimal interface for any provider.
- LiteLLMProvider preserves the existing API-based behavior.
- The node layer now delegates to a provider instance, so future browser-based providers can be plugged in without changing the engine protocol flow.
