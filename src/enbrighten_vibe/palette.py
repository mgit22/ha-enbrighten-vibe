"""
Palette model for the Enbrighten Vibe protocol.

A Palette is an ordered sequence of one to six Colors.

Rules:
- At least one Color is required.
- At most six Colors are permitted.
- Order is preserved.
- Duplicate Colors are allowed.
"""

from __future__ import annotations

from collections.abc import Iterator
from dataclasses import dataclass, field

from .colors import Color


@dataclass(frozen=True, slots=True)
class Palette:
    """Represents an ordered sequence of Colors."""

    _colors: tuple[Color, ...] = field(init=False, repr=False)

    def __init__(self, *colors: Color) -> None:
        """Create a Palette from one to six Colors."""

        if not 1 <= len(colors) <= 6:
            raise ValueError("A Palette must contain between 1 and 6 Colors.")

        object.__setattr__(self, "_colors", tuple(colors))

    def __len__(self) -> int:
        """Return the number of Colors in the Palette."""

        return len(self._colors)

    def __iter__(self) -> Iterator[Color]:
        """Iterate over the Colors in the Palette."""

        return iter(self._colors)

    def __getitem__(self, index: int) -> Color:
        """Return the Color at the specified index."""

        return self._colors[index]

    def __repr__(self) -> str:
        """Return a readable representation of the Palette."""

        colors = ", ".join(repr(color) for color in self._colors)
        return f"Palette({colors})"