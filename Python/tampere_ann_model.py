# -*- coding: utf-8 -*-
"""tampere_ANN_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ku0ds_iP7YoHZv5WF0-HcgI_cRkceoX0
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters for the sine wave
Fs = 1000  # Sampling frequency in Hz
T = 1 / Fs  # Sampling period in seconds
L = 1000  # Length of the signal (number of samples)
t = np.arange(0, L) * T  # Time vector

f = 50  # Frequency of the sine wave in Hz
A = 0.4  # Amplitude of the sine wave

# Generating the sine wave
y = A * np.sin(2 * np.pi * f * t)

# Plotting the sine wave
plt.figure()
plt.plot(t, y)
plt.title('Sine Wave')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)



plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Parameters for the sine wave
Fs = 1000  # Sampling frequency in Hz
T = 1 / Fs  # Sampling period in seconds
L = 1500  # Length of the signal (number of samples)
t = np.arange(0, L) * T  # Time vector

f = 50  # Frequency of the sine wave in Hz
A = 0.7  # Amplitude of the sine wave

# Generate sine wave with harmonics
X = A * np.sin(2 * np.pi * f * t)  # Fundamental frequency
numHarmonics = 3  # Number of harmonics to add

# Adjusting the amplitude and phase shift for each harmonic
for n in range(2, numHarmonics + 2):  # Python's range is exclusive at the end, so we add 2
    harmonicAmplitude = A / (2 * n)  # Decreasing amplitude for each harmonic
    harmonicPhaseShift = -np.pi / 2  # Setting phase shift to -90 degrees for all harmonics
    X += harmonicAmplitude * np.sin(2 * np.pi * f * n * t + harmonicPhaseShift)

# Plotting the sine wave with harmonics
plt.figure(figsize=(55, 8))
plt.plot(t, X)
plt.title('Sine Wave with Harmonics')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)

# Optional: Adjust y-axis to spread the plot vertically if needed
plt.ylim([-A, A])  # Adjust as needed based on the added harmonics

plt.show()



import numpy as np
import matplotlib.pyplot as plt

# Assuming X, t, and Fs are defined from the sine wave generation with harmonics

# Compute the FFT directly
Y = np.fft.fft(X)  # FFT of the signal
P2 = np.abs(Y/L)  # Two-sided spectrum
P1 = P2[:L//2+1]  # Single-sided spectrum, as the signal is real
P1[1:-1] *= 2  # Correct the amplitude for the single-sided spectrum

# Frequency axis
f = Fs * np.arange(0, (L//2+1))/L

# Plot the FFT
plt.figure(figsize=(55, 8))
plt.plot(f, P1)
plt.title('Single-Sided Amplitude Spectrum of X(t)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()

from scipy.fft import fft
import numpy as np
import matplotlib.pyplot as plt

# Assuming the sine wave with harmonics 'X', sampling frequency 'Fs', and signal length 'L' are defined

# Compute the FFT using scipy's fft function
Y = fft(X)  # FFT of the signal
P2 = np.abs(Y / L)  # Two-sided spectrum
P1 = P2[:L//2+1]  # Single-sided spectrum for real-valued signal
P1[1:-1] *= 2  # Correct the amplitude for non-DC and non-Nyquist components

# Frequency axis
f = Fs * np.arange(0, (L//2+1)) / L

# Plotting the FFT
plt.figure(figsize=(55, 8))
plt.plot(f, P1)
plt.title('Single-Sided Amplitude Spectrum of X(t)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.show()









import numpy as np
import matplotlib.pyplot as plt



frequency = 5  # Frequency of the sine wave in Hz
amplitude = 1  # Amplitude of the sine wave
sampling_rate = 100  # Sampling rate in Hz
duration = 2  # Duration in seconds


t = np.arange(0, duration, 1 / sampling_rate)  # Time vector
y = amplitude * np.sin(2 * np.pi * frequency * t)  # Sine wave formula



plt.figure(figsize=(10, 4))
plt.plot(t, y)
plt.title('Sine Wave')
plt.xlabel('Time [s]')
plt.ylabel('Amplitude')
plt.grid(True)
plt.show()



import numpy as np
import matplotlib.pyplot as plt

def generate_sine_wave(freq, amplitude, sampling_freq, length):
    T = 1 / sampling_freq
    t = np.arange(0, length) * T
    return t, amplitude * np.sin(2 * np.pi * freq * t)

def add_harmonics(base_wave, num_harmonics, fundamental_freq, amplitude, sampling_freq):
    t, X = base_wave
    for n in range(2, num_harmonics + 2):
        harmonic_amplitude = amplitude / np.sqrt(n)  # Adjust the amplitude decay rate here
        harmonic_freq = fundamental_freq * n
        X += harmonic_amplitude * np.sin(2 * np.pi * harmonic_freq * t)
    return t, X

# Parameters
Fs = 1000  # Sampling frequency in Hz
L = 1500  # Length of the signal
f = 50  # Frequency of the sine wave in Hz
A = 0.7  # Amplitude of the sine wave
num_harmonics = 3

# Generate base sine wave
t, base_wave = generate_sine_wave(f, A, Fs, L)

# Add harmonics
t, X = add_harmonics((t, base_wave), num_harmonics, f, A, Fs)

# Plotting
plt.figure(figsize=(55, 6))
plt.plot(t, X, label='Sine Wave with Harmonics')
plt.title('Sine Wave with Harmonics')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.ylim([-A*2, A*2])  # Adjust based on the maximum amplitude observed
plt.legend()
plt.show()

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import matplotlib.pyplot as plt

# Generate sinusoidal data
time_extended = np.linspace(0, 20 * 2 * np.pi, 2000)
correct_data_extended = np.sin(time_extended)
noise_extended = np.random.normal(0, 0.2, correct_data_extended.shape)
faulty_data_extended = correct_data_extended + noise_extended

# Convert to PyTorch tensors
correct_data_tensor = torch.tensor(correct_data_extended.reshape(-1, 1), dtype=torch.float32)
faulty_data_tensor = torch.tensor(faulty_data_extended.reshape(-1, 1), dtype=torch.float32)

# Create a dataset and dataloader
dataset = TensorDataset(faulty_data_tensor, correct_data_tensor)
dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

# Enhanced model architecture
class EnhancedSinusoidalDenoisingModel(nn.Module):
    def __init__(self):
        super(EnhancedSinusoidalDenoisingModel, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(1, 128),  # Increased width
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1)   # Output layer
        )

    def forward(self, x):
        return self.network(x)

# Initialize the enhanced model, loss function, and optimizer
model = EnhancedSinusoidalDenoisingModel()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)  # Adjust learning rate if needed

# Training
epochs = 200  # Increased number of epochs
for epoch in range(epochs):
    for faulty, correct in dataloader:
        optimizer.zero_grad()
        outputs = model(faulty)
        loss = criterion(outputs, correct)
        loss.backward()
        optimizer.step()

    if epoch % 20 == 19:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

# Prediction example (adjust as needed for your specific use case)
with torch.no_grad():
    predicted_corrected_data = model(faulty_data_tensor).numpy()

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(time_extended, correct_data_extended, label='Original Correct Data', alpha=0.75)
plt.plot(time_extended, faulty_data_extended, label='Given Faulty Data', linestyle='--', alpha=0.75)
plt.plot(time_extended, predicted_corrected_data.flatten(), label='Model Corrected Data', alpha=0.75)
plt.title('Sinusoidal Data: Original, Faulty, and Corrected by Model')
plt.xlabel('Time')
plt.ylabel('Magnitude')
plt.legend()
plt.show()

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import matplotlib.pyplot as plt

# Generate sinusoidal data
time_extended = np.linspace(0, 20 * 2 * np.pi, 2000)
correct_data_extended = np.sin(time_extended)
noise_extended = np.random.normal(0, 0.2, correct_data_extended.shape)
faulty_data_extended = correct_data_extended + noise_extended

# Convert to PyTorch tensors
correct_data_tensor = torch.tensor(correct_data_extended.reshape(-1, 1), dtype=torch.float32)
faulty_data_tensor = torch.tensor(faulty_data_extended.reshape(-1, 1), dtype=torch.float32)

# Create a dataset and dataloader
dataset = TensorDataset(faulty_data_tensor, correct_data_tensor)
dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

# Enhanced model architecture
class EnhancedSinusoidalDenoisingModel(nn.Module):
    def __init__(self):
        super(EnhancedSinusoidalDenoisingModel, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(1, 128),  # Increased width
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1)   # Output layer
        )

    def forward(self, x):
        return self.network(x)

# Initialize the enhanced model, loss function, and optimizer
model = EnhancedSinusoidalDenoisingModel()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)  # Adjust learning rate if needed

# Training
epochs = 200  # Increased number of epochs
for epoch in range(epochs):
    for faulty, correct in dataloader:
        optimizer.zero_grad()
        outputs = model(faulty)
        loss = criterion(outputs, correct)
        loss.backward()
        optimizer.step()

    if epoch % 20 == 19:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

# Prediction example (adjust as needed for your specific use case)
with torch.no_grad():
    predicted_corrected_data = model(faulty_data_tensor).numpy()


# Assuming `time_extended`, `correct_data_extended`, `faulty_data_extended`, and `predicted_corrected_data` are defined as before

# Enhancing the plot
plt.figure(figsize=(15, 7))  # Increase the figure size

# Plot original correct data with a solid line
plt.plot(time_extended, correct_data_extended, label='Original Correct Data', color='blue', linewidth=2.5, alpha=0.8)

# Plot given faulty data with a dotted line
plt.plot(time_extended, faulty_data_extended, label='Given Faulty Data', color='orange', linestyle=':', linewidth=1, alpha=0.6)

# Plot model corrected data with a dashed line
plt.plot(time_extended, predicted_corrected_data.flatten(), label='Model Corrected Data', color='green', linestyle='--', linewidth=2.5, alpha=0.8)

# Add grid, title, labels, and legend
plt.grid(True)
plt.title('Sinusoidal Data: Original, Faulty, and Corrected by Model', fontsize=16)
plt.xlabel('Time', fontsize=14)
plt.ylabel('Magnitude', fontsize=14)
plt.legend(fontsize=12)
plt.show()

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import matplotlib.pyplot as plt

# Generate sinusoidal data
time_extended = np.linspace(0, 20 * 2 * np.pi, 2000)
correct_data_extended = np.sin(time_extended)
noise_extended = np.random.normal(0, 0.2, correct_data_extended.shape)
faulty_data_extended = correct_data_extended + noise_extended

# Convert to PyTorch tensors
correct_data_tensor = torch.tensor(correct_data_extended.reshape(-1, 1), dtype=torch.float32)
faulty_data_tensor = torch.tensor(faulty_data_extended.reshape(-1, 1), dtype=torch.float32)

# Create a dataset and dataloader
dataset = TensorDataset(faulty_data_tensor, correct_data_tensor)
dataloader = DataLoader(dataset, batch_size=64, shuffle=True)

# Enhanced model architecture
class EnhancedSinusoidalDenoisingModel(nn.Module):
    def __init__(self):
        super(EnhancedSinusoidalDenoisingModel, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(1, 128),  # Increased width
            nn.ReLU(),
            nn.Linear(128, 128),
            nn.ReLU(),
            nn.Linear(128, 64),
            nn.ReLU(),
            nn.Linear(64, 1)   # Output layer
        )

    def forward(self, x):
        return self.network(x)

# Initialize the enhanced model, loss function, and optimizer
model = EnhancedSinusoidalDenoisingModel()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)  # Adjust learning rate if needed

# Training
epochs = 600  # Increased number of epochs
for epoch in range(epochs):
    for faulty, correct in dataloader:
        optimizer.zero_grad()
        outputs = model(faulty)
        loss = criterion(outputs, correct)
        loss.backward()
        optimizer.step()

    if epoch % 20 == 19:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')

# Prediction example (adjust as needed for your specific use case)
with torch.no_grad():
    predicted_corrected_data = model(faulty_data_tensor).numpy()




# Assuming 'time_extended', 'correct_data_extended', 'faulty_data_extended', and 'predicted_corrected_data' are defined

# Plotting each sinusoidal signal separately for clarity
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 15), sharex=True)

# Original Correct Data
axes[0].plot(time_extended, correct_data_extended, color='blue')
axes[0].set_title('Original Correct Sinusoidal Data')
axes[0].set_ylabel('Magnitude')
axes[0].grid(True)

# Given Faulty Data
axes[1].plot(time_extended, faulty_data_extended, color='orange')
axes[1].set_title('Given Faulty Sinusoidal Data')
axes[1].set_ylabel('Magnitude')
axes[1].grid(True)

# Model Corrected Data
axes[2].plot(time_extended, predicted_corrected_data.flatten(), color='green')
axes[2].set_title('Model Corrected Sinusoidal Data')
axes[2].set_xlabel('Time')
axes[2].set_ylabel('Magnitude')
axes[2].grid(True)

plt.tight_layout()
plt.show()

import numpy as np
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset
import matplotlib.pyplot as plt

# Generate sinusoidal data
time_extended = np.linspace(0, 20 * 2 * np.pi, 2000)
correct_data_extended = np.sin(time_extended)
noise_extended = np.random.normal(0, 0.2, correct_data_extended.shape)
faulty_data_extended = correct_data_extended + noise_extended

# Convert to PyTorch tensors
correct_data_tensor = torch.tensor(correct_data_extended.reshape(-1, 1), dtype=torch.float32)
faulty_data_tensor = torch.tensor(faulty_data_extended.reshape(-1, 1), dtype=torch.float32)

# Create a dataset and dataloader
dataset = TensorDataset(faulty_data_tensor, correct_data_tensor)
dataloader = DataLoader(dataset, batch_size=64, shuffle=True)







# ... [previous setup code with data generation and tensor conversion] ...

# Enhanced model architecture with additional layers and neurons
class EnhancedSinusoidalDenoisingModel(nn.Module):
    def __init__(self):
        super(EnhancedSinusoidalDenoisingModel, self).__init__()
        self.network = nn.Sequential(
            nn.Linear(1, 256),  # Increased width
            nn.LeakyReLU(0.01),  # Changed activation function
            nn.Linear(256, 128),
            nn.LeakyReLU(0.01),
            nn.Dropout(0.1),  # Added dropout for regularization
            nn.Linear(128, 128),
            nn.LeakyReLU(0.01),
            nn.Linear(128, 64),
            nn.LeakyReLU(0.01),
            nn.Linear(64, 1)
        )

    def forward(self, x):
        return self.network(x)

# Initialize the model
model = EnhancedSinusoidalDenoisingModel()

# Using Smooth L1 Loss as an alternative to MSE
criterion = nn.SmoothL1Loss()

# Optimizer with weight decay for L2 regularization
optimizer = optim.Adam(model.parameters(), lr=0.001, weight_decay=1e-5)

# Implementing a learning rate scheduler that decreases the learning rate over epochs
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=50, gamma=0.5)

# Training with a modified batch size
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)  # Smaller batch size

# Training loop with scheduler step update
epochs = 200
for epoch in range(epochs):
    for faulty, correct in dataloader:
        optimizer.zero_grad()
        outputs = model(faulty)
        loss = criterion(outputs, correct)
        loss.backward()
        optimizer.step()
    scheduler.step()  # Update the learning rate

    if epoch % 20 == 19:
        print(f'Epoch [{epoch+1}/{epochs}], Loss: {loss.item():.4f}')








# Prediction example (adjust as needed for your specific use case)
with torch.no_grad():
    predicted_corrected_data = model(faulty_data_tensor).numpy()




# Assuming 'time_extended', 'correct_data_extended', 'faulty_data_extended', and 'predicted_corrected_data' are defined

# Plotting each sinusoidal signal separately for clarity
fig, axes = plt.subplots(nrows=3, ncols=1, figsize=(12, 15), sharex=True)

# Original Correct Data
axes[0].plot(time_extended, correct_data_extended, color='blue')
axes[0].set_title('Original Correct Sinusoidal Data')
axes[0].set_ylabel('Magnitude')
axes[0].grid(True)

# Given Faulty Data
axes[1].plot(time_extended, faulty_data_extended, color='orange')
axes[1].set_title('Given Faulty Sinusoidal Data')
axes[1].set_ylabel('Magnitude')
axes[1].grid(True)

# Model Corrected Data
axes[2].plot(time_extended, predicted_corrected_data.flatten(), color='green')
axes[2].set_title('Model Corrected Sinusoidal Data')
axes[2].set_xlabel('Time')
axes[2].set_ylabel('Magnitude')
axes[2].grid(True)

plt.tight_layout()
plt.show()

