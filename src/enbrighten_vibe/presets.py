"""
Preset definitions for the Enbrighten Vibe protocol.

A Preset is a named, reusable State.

This module also defines the PresetCode model used by the DP106
State. The semantics of individual Preset Codes are still being
reverse engineered, so PresetCode currently stores only the raw
protocol value.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .state import State


@dataclass(frozen=True, slots=True)
class PresetCode:
    """Represents the Preset Code portion of a State."""

    code: int

    def __post_init__(self) -> None:
        """Validate the protocol value."""

        if not 0 <= self.code <= 0xFF:
            raise ValueError("Preset Code must be between 0x00 and 0xFF.")


# Convenience constant used by the integration.
PresetCode.Custom = PresetCode(0xFF)


@dataclass(frozen=True, slots=True)
class Preset:
    """Represents a named, reusable State."""

    name: str
    state: State