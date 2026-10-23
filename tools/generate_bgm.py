"""Generate two original short test loops; requires ffmpeg on PATH."""
from pathlib import Path
import math, struct, subprocess, wave

ROOT = Path(__file__).resolve().parents[1]
SR = 22050
SECONDS = 16

def render(name, notes, chords):
    samples = []
    for i in range(SR * SECONDS):
        t = i / SR
        step = int(t / 0.5)
        u = t % 0.5
        f = 440 * 2 ** ((notes[step % len(notes)] - 69) / 12)
        envelope = min(1, u / 0.012) * math.exp(-u * 6) * min(1, (0.5 - u) / 0.025)
        melody = (math.sin(2 * math.pi * f * u) + .15 * math.sin(4 * math.pi * f * u)) * envelope
        chord = chords[int(t // 4) % len(chords)]
        pad = sum(math.sin(2 * math.pi * (440 * 2 ** ((n - 69) / 12)) * t) for n in chord) / 3
        edge = min(1, t / .12, (SECONDS - t) / .22)
        samples.append(int(32767 * edge * (.20 * melody + .055 * pad)))
    wav_path = ROOT / 'bgm' / (name + '.wav')
    with wave.open(str(wav_path), 'wb') as out:
        out.setnchannels(1)
        out.setsampwidth(2)
        out.setframerate(SR)
        out.writeframes(struct.pack('<' + 'h' * len(samples), *samples))
    subprocess.run(['ffmpeg', '-y', '-v', 'error', '-i', str(wav_path), '-codec:a', 'libmp3lame', '-b:a', '32k', str(wav_path.with_suffix('.mp3'))], check=True)

render('house-test', [60,64,67,72,67,64,62,67,65,69,72,69,67,64,62,60], [[48,52,55],[53,57,60],[55,59,62],[48,52,55]])
render('garden-test', [69,72,76,72,67,71,74,71,65,69,72,69,64,67,71,67], [[45,48,52],[43,47,50],[41,45,48],[40,43,47]])
