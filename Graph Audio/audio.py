import numpy as np
import sounddevice as sd

fs = 44100
phase = 0.0
frequency = 220.0  # start frequency

def callback(outdata, frames, time, status):
    global phase, frequency
    t = np.arange(frames) / fs
    # Generate sine wave at current frequency
    wave = np.sin(2 * np.pi * frequency * t + phase)
    phase += 2 * np.pi * frequency * frames / fs
    outdata[:] = wave.reshape(-1, 1)

# Start stream
stream = sd.OutputStream(callback=callback, samplerate=fs, channels=1)
stream.start()

# Change pitch over time
import time
for f in np.linspace(220, 880, 4):  # sweep 50 steps
    frequency = f
    time.sleep(0.1)

stream.stop()
