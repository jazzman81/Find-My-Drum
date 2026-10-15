"""Render approximate chip-melody WAV previews, independent of Arcade playback."""
import ast
import math
from pathlib import Path
import re
import struct
import wave

ROOT = Path(__file__).resolve().parent
RATE = 22050
TRACKS = [('MEADOW_TRACK', 'Lantern-Bounce', 176, 'triangle'),
          ('QUARRY_TRACK', 'Quarry-Pocket', 192, 'square'),
          ('GROVE_TRACK', 'Moonlit-Return', 168, 'sine')]
values = {node.targets[0].id: ast.literal_eval(node.value)
          for node in ast.parse((ROOT / 'soundtrack.py').read_text()).body
          if isinstance(node, ast.Assign) and isinstance(node.value, ast.Constant)
          and isinstance(node.value.value, str)}
output = ROOT / 'audio-previews'
output.mkdir(exist_ok=True)
for constant, title, tempo, shape in TRACKS:
    pcm = bytearray()
    for token in values[constant].split():
        match = re.fullmatch(r'([A-GR])(#?)([0-8]?):([0-9]+)', token)
        if not match:
            continue
        note, sharp, octave, beats = match.groups()
        duration = int(beats) * 60 / tempo
        count = round(duration * RATE)
        if note == 'R':
            pcm.extend(bytes(count * 2))
            continue
        midi = (int(octave or 4) + 1) * 12 + {'C':0,'D':2,'E':4,'F':5,'G':7,'A':9,'B':11}[note] + bool(sharp)
        frequency = 440 * 2 ** ((midi - 69) / 12)
        for sample in range(count):
            t = sample / RATE
            phase = (t * frequency) % 1
            signal = math.sin(2 * math.pi * phase)
            if shape == 'square':
                signal = 0.7 if phase < 0.5 else -0.7
            elif shape == 'triangle':
                signal = 1 - 4 * abs(phase - 0.5)
            envelope = min(1, t / 0.012, (duration - t) / 0.055)
            pcm.extend(struct.pack('<h', round(signal * max(0, envelope) * 6500)))
    destination = output / (title + '.wav')
    with wave.open(str(destination), 'wb') as stream:
        stream.setnchannels(1)
        stream.setsampwidth(2)
        stream.setframerate(RATE)
        stream.writeframes(pcm)
    print(destination.name, round(len(pcm) / (RATE * 2), 2), 'seconds')
