import sounddevice as sd
import numpy as np
import wave
def record_audio(duration, filename, device=3):
    sample_rate = 48000  # Change to a supported sample rate

    print("Recording...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16', device=device)
    sd.wait()
    print("Recording finished.")


if __name__ == "__main__":
    record_duration = 5  # Duration in seconds
    output_filename = 'recorded_audio.wav'
    record_audio(record_duration, output_filename)
