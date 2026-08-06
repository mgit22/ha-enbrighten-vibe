"""
State model for the Enbrighten Vibe protocol.

A State represents the complete DP106 Lighting State exchanged with
the controller. It contains all information required to render an
effect, including the Preset Code, Effect, Speed, Brightness, and
Palette.

Encoding and decoding are handled separately.
"""

from __future__ import annotations

from dataclasses import dataclass

from .effects import Effect
from .palette import Palette
from .presets import PresetCode


@dataclass(frozen=True, slots=True)
class State:
    """Represents a complete DP106 Lighting State."""

    preset_code: PresetCode
    effect: Effect
    brightness: int
    speed: int
    palette: Palette

    def __post_init__(self) -> None:
        """Validate the State."""

        if not 1 <= self.brightness <= 100:
            raise ValueError("Brightness must be between 1 and 100 percent.")

        if not 1 <= self.speed <= 100:
            raise ValueError("Speed must be between 1 and 100 percent.")