import logging
import wave
import os
import matplotlib.pyplot as plt
import numpy as np
import scipy


# create f0= 440 Hz wave ,1s, 1A, Abtastrate 20*f0
# 2nd harmonic	880 hertz, 3rd  harmonic 3*440

def create_sine_wave(filename, frequency, duration, amplitude, sample_rate=16000):
    if (os.path.exists(filename)):
        print("File already exists")
    else:
        t = np.linspace(0, duration, int(sample_rate * duration))  # Time axis
        wave = amplitude * np.sin(2 * np.pi * frequency * t)
        scipy.io.wavfile.write(f"{filename}.wav", sample_rate, data=wave.astype(np.int16))


def plot_sound_signal(*paths_to_wav):
    for path_to_wav in paths_to_wav:
        # spf = wave.open(path_to_wav, "rb")
        samplerate, spf = scipy.io.wavfile.read(path_to_wav)
        plt.plot(spf)
        # Extract Raw Audio from Wav File
        plt.ylabel("Signal Value")
        plt.xlabel("Times(s)")
        plt.grid()
        plt.show()


def main():
    # plot_sound_signal("test_sound.wav")
    create_sine_wave("F0", amplitude=1, sample_rate=440 * 20, frequency=440,duration=1)
    create_sine_wave("F1", frequency=880, amplitude=1, sample_rate=440 * 20,duration=1)
    create_sine_wave("F2", frequency=440 * 3, amplitude=1, sample_rate=440 * 20,duration=1)
    plot_sound_signal("F0.wav","F1.wav","F2.wav")


if __name__ == "__main__":
    main()
