import sounddevice as sd
import soundfile as sf
import librosa
import numpy as np
import queue
import os
from datetime import datetime

SAMPLE_RATE = 44100
CHANNELS = 1

audio_queue = queue.Queue()
recording = True

os.makedirs("source", exist_ok=True)
os.makedirs("result", exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

source_path = f"source/input_{timestamp}.wav"
result_path = f"result/output_{timestamp}.wav"

recorded_audio = []

def callback(indata, frames, time, status):
    if recording:
        recorded_audio.append(indata.copy())

print("Recording...")
print("Press ENTER to stop.")

stream = sd.InputStream(
    samplerate=SAMPLE_RATE,
    channels=CHANNELS,
    callback=callback
)

stream.start()

input()

recording = False
stream.stop()
stream.close()

audio = np.concatenate(recorded_audio, axis=0)

# save original audio
sf.write(source_path, audio, SAMPLE_RATE)

print("Original saved.")

# load and process
y, sr = librosa.load(source_path, sr=SAMPLE_RATE)

# male -> female
y_changed = librosa.effects.pitch_shift(
    y=y,
    sr=sr,
    n_steps=6
)

# save result
sf.write(result_path, y_changed, sr)

print("Converted saved.")

# play result
print("Playing converted voice...")
sd.play(y_changed, sr)
sd.wait()

print("Done.")
print("Source:", source_path)
print("Result:", result_path)