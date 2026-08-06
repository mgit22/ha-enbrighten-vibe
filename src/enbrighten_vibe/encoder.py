"""
Encoder for the Enbrighten Vibe protocol.

This module converts a State into the DP106 payload understood by the
Enbrighten Vibe controller.
"""

from __future__ import annotations

from .state import State


def encode(state: State) -> str:
    """
    Encode a State into a DP106 payload.

    Args:
        state:
            The State to encode.

    Returns:
        The encoded DP106 payload.

    Raises:
        NotImplementedError:
            Encoding has not yet been implemented.
    """

    raise NotImplementedError("State encoding has not yet been implemented.")