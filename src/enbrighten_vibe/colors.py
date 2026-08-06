"""
Color definitions for the Enbrighten Vibe protocol.

This module defines the Color model along with common named colors
used by the Enbrighten Vibe ecosystem.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import ClassVar


@dataclass(frozen=True, slots=True)
class Color:
    """Represents a single RGB color."""

    red: int
    green: int
    blue: int

    def __post_init__(self) -> None:
        """Validate RGB component values."""

        for value in (self.red, self.green, self.blue):
            if not 0 <= value <= 255:
                raise ValueError("RGB values must be between 0 and 255.")

    @classmethod
    def from_rgb(cls, red: int, green: int, blue: int) -> "Color":
        """Create a Color from RGB values."""

        return cls(red, green, blue)

    @classmethod
    def from_hex(cls, value: str) -> "Color":
        """Create a Color from a hexadecimal RGB string."""

        value = value.strip().lstrip("#")

        if len(value) != 6:
            raise ValueError("Hex color must contain exactly six hexadecimal digits.")

        return cls(
            int(value[0:2], 16),
            int(value[2:4], 16),
            int(value[4:6], 16),
        )

    # Common named colors (Smart Life defaults)
    Red: ClassVar["Color"]
    Orange: ClassVar["Color"]
    Yellow: ClassVar["Color"]
    Green: ClassVar["Color"]
    Blue: ClassVar["Color"]
    Purple: ClassVar["Color"]
    Pink: ClassVar["Color"]
    White: ClassVar["Color"]


# Initialize the named colors
Color.Red = Color(255, 0, 0)
Color.Orange = Color(255, 70, 0)
Color.Yellow = Color(250, 230, 0)
Color.Green = Color(0, 255, 0)
Color.Blue = Color(0, 0, 255)
Color.Purple = Color(156, 35, 242)
Color.Pink = Color(255, 32, 0)
Color.White = Color(255, 255, 255)