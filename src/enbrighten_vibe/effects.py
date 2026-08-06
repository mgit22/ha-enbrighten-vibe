"""
Effect definitions for the Enbrighten Vibe protocol.

The Effect ID is the second byte of the DP106 Lighting State and
determines how the Palette is rendered.
"""

from enum import IntEnum


class Effect(IntEnum):
    """Known Enbrighten Vibe lighting effects."""

    Solid = 0x00
    Twinkle = 0x01
    Strobe = 0x02
    Pulse = 0x03
    Chase = 0x05
    Wave = 0x06
    FadeShift = 0x07
    Lightning = 0x08
    Flame = 0x09
    Vibe = 0x11
    Morph = 0x12
    Drift = 0x13
    Shimmer = 0x15
    FadeMelt = 0x16