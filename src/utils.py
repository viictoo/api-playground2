"""Tiny utilities used by main."""


def greet(name: str) -> str:
    """Return a friendly greeting."""
    if not name:
        raise ValueError("name must be non empty")
    return f"Hello, {name}!"


def shout(name: str) -> str:
    return greet(name).upper()
