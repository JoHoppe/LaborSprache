import matplotlib.pyplot as plt
import numpy as np
import wave
import sys
import logging

logging.basicConfig()

def plot_sound_signal(path_to_wav):
    spf = wave.open(path_to_wav, "rb")

    # Extract Raw Audio from Wav File
    sample_samples = spf.getnframes()
    sample_signal = spf.readframes(sample_samples)
    sample_frequency = spf.getframerate()
    sample_signal_wave = spf.readframes(sample_samples)
    signal_array = np.frombuffer(sample_signal, np.int16)
    times = np.linspace(0, sample_samples / sample_frequency, num=sample_samples)
    t_audio = sample_samples / sample_frequency

    plt.figure(figsize=(15, 5))
    plt.plot(times, signal_array)
    plt.ylabel("Signal Value")
    plt.xlabel("Times(s)")
    plt.xlim(0, t_audio)
    plt.show()
def main():
    plot_sound_signal("test_sound.wav")
if __name__ =="__main__":
    main()
