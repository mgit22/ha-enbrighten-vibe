"""
Example demonstrating creation of a Christmas preset and encoding it
into a DP106 payload.
"""

from enbrighten_vibe.colors import Color
from enbrighten_vibe.effects import Effect
from enbrighten_vibe.encoder import encode
from enbrighten_vibe.palette import Palette
from enbrighten_vibe.presets import Preset, PresetCode
from enbrighten_vibe.state import State


print("Starting...")

christmas = Preset(
    name="Christmas",
    state=State(
        preset_code=PresetCode.Custom,
        effect=Effect.Twinkle,
        brightness=100,
        speed=50,
        palette=Palette(
            Color.Red,
            Color.Green,
            Color.Yellow,
            Color.Blue,
        ),
    ),
)

print("Preset created successfully.\n")

print(christmas)

print("\nEncoded DP106 payload:")
print(encode(christmas.state))

print("\nFinished.")