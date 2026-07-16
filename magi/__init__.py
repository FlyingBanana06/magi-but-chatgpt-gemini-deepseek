__version__ = "0.1.0"


def __getattr__(name):
    if name == "MAGI":
        from magi.core.engine import MAGI
        return MAGI
    raise AttributeError(name)


__all__ = ["MAGI"]
