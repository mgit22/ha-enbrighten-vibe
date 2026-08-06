"""Lighting State (DP106) implementation."""

from dataclasses import dataclass


@dataclass(slots=True)
class LightingState:
    """Represents an Enbrighten Vibe DP106 Lighting State."""
    