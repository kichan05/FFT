import numpy as np

def fft(signal):
    N = len(signal)
    half = N // 2

    if(N == 1):
        return signal

    X_even = fft(signal[::2])
    X_odd = fft(signal[1::2])

    W = np.exp(-2j * np.pi * np.arange(N) / N)
    new_signal = np.zeros_like(signal, dtype=complex)

    new_signal[:half] = X_even + W[:half] * X_odd
    new_signal[half:] = X_even - W[:half] * X_odd

    return new_signal