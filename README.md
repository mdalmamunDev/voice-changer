# 🎙️ Voice Pitch Shifter

A simple Python script that records your voice in real time, shifts the pitch (male → female), saves both the original and converted audio, and plays back the result.

---

## 📁 Project Structure

```
project/
├── main.py          # Main script
├── source/          # Auto-created — stores original recordings
└── result/          # Auto-created — stores pitch-shifted output
```

---

## ⚙️ Requirements

### Python Version
Python 3.7+

### Dependencies

Install all required packages via pip:

```bash
pip install sounddevice soundfile librosa numpy
```

| Package       | Purpose                              |
|---------------|--------------------------------------|
| `sounddevice` | Record and play audio in real time   |
| `soundfile`   | Read/write WAV audio files           |
| `librosa`     | Audio analysis and pitch shifting    |
| `numpy`       | Numerical operations on audio data   |

> **Note:** `sounddevice` requires PortAudio. Install it if needed:
> - **Ubuntu/Debian:** `sudo apt-get install libportaudio2`
> - **macOS:** `brew install portaudio`
> - **Windows:** Usually bundled automatically.

---

## 🚀 Usage

Run the script:

```bash
python main.py
```

1. The script starts recording immediately from your default microphone.
2. Press **ENTER** to stop recording.
3. The original audio is saved to `source/`.
4. The pitch-shifted audio is saved to `result/`.
5. The converted audio plays back automatically.

---

## 🔧 Configuration

At the top of `main.py`, you can adjust these constants:

| Constant      | Default  | Description                          |
|---------------|----------|--------------------------------------|
| `SAMPLE_RATE` | `44100`  | Audio sample rate in Hz              |
| `CHANNELS`    | `1`      | Number of audio channels (1 = mono)  |

To change the pitch shift amount, edit the `n_steps` parameter in the `pitch_shift` call:

```python
y_changed = librosa.effects.pitch_shift(
    y=y,
    sr=sr,
    n_steps=6   # Positive = higher pitch, Negative = lower pitch
)
```

| `n_steps` | Effect                        |
|-----------|-------------------------------|
| `+6`      | Male → Female (default)       |
| `+12`     | One full octave up            |
| `-6`      | Female → Male                 |
| `-12`     | One full octave down          |

---

## 📂 Output Files

Files are named with a timestamp to avoid overwriting:

```
source/input_20240522_143000.wav
result/output_20240522_143000.wav
```

---

## 📝 Notes

- The script uses your system's **default microphone**. Make sure it is connected and permitted.
- Processing time depends on the length of the recording and your hardware.
- Pitch shifting is performed offline after recording stops.