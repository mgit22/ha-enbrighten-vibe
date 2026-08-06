"""
Encoder for the Enbrighten Vibe protocol.

This module converts a State into the DP106 payload understood by the
Enbrighten Vibe controller.
"""

from __future__ import annotations

from .colors import Color
from .effects import Effect
from .palette import Palette
from .presets import PresetCode
from .state import State


def encode(state: State) -> str:
    """
    Encode a State into a DP106 payload.
    """

    parts = [
        _encode_preset_code(state.preset_code),
        _encode_effect(state.effect),
        _encode_speed(state.speed),
        _encode_brightness(state.brightness),
        _encode_palette(state.palette),
    ]

    return "".join(parts)


def _encode_preset_code(preset_code: PresetCode) -> str:
    """Encode the Preset Code."""

    return _to_hex(preset_code.code, 2)


def _encode_effect(effect: Effect) -> str:
    """Encode the Effect."""

    return _to_hex(effect.value, 2)


def _encode_speed(speed: int) -> str:
    """Encode the Speed."""

    return _to_hex(_percent_to_protocol(speed), 4)


def _encode_brightness(brightness: int) -> str:
    """Encode the Brightness."""

    return _to_hex(_percent_to_protocol(brightness), 4)


def _encode_palette(palette: Palette) -> str:
    """
    Encode a Palette.
    """

    parts = [
        _to_hex(len(palette), 1),
    ]

    for color in palette:
        parts.append(_encode_color(color))

    return "".join(parts)


def _encode_color(color: Color) -> str:
    """
    Encode a Color.
    """

    return (
        "#00"
        + _to_hex(color.red, 2)
        + _to_hex(color.green, 2)
        + _to_hex(color.blue, 2)
    )


def _percent_to_protocol(percent: int) -> int:
    """
    Convert a percentage (1–100) into the protocol value (10–1000).
    """

    return round(percent * 10)


def _to_hex(value: int, width: int) -> str:
    """
    Convert an integer to a zero-padded lowercase hexadecimal string.
    """

    return f"{value:0{width}x}"