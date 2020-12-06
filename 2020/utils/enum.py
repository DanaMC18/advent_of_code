"""A utility for creating enum-like objects."""

from collections import namedtuple


def enum(name, **elements):
    """Create a new enum."""
    enum_meta = namedtuple(name, elements.keys())
    return enum_meta(**elements)
