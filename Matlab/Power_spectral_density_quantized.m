% Parameters for the sine wave
Fs = 1000;             % Sampling frequency in Hz
T = 1/Fs;              % Sampling period in seconds
L = 1500;              % Length of the signal (number of samples)
t = (0:L-1)*T;         % Time vector

f = 50;                % Frequency of the sine wave in Hz
A = 0.7;               % Amplitude of the sine wave

% Generate sine wave with harmonics
X = A * sin(2 * pi * f * t);   % Fundamental frequency
numHarmonics = 3;              % Number of harmonics to add

% Adjusting the amplitude and phase shift for each harmonic
for n = 2:numHarmonics+1
    harmonicAmplitude = A / (4*n);            % Decreasing amplitude for each harmonic
    harmonicPhaseShift = -pi/2;               % Setting phase shift to -90 degrees for all harmonics
    X = X + harmonicAmplitude * sin(2 * pi * f * n * t + harmonicPhaseShift);
end


% Quantization

% Quantization parameters
n = 6;
L_quant = 2^n - 1;

% Quantized the signal
X_min = min(X);
X_max = max(X);
Delta = (X_max - X_min) / L_quant;
X_quantized = round((X - X_min) / Delta) * Delta + X_min;




% Compute the Fast Fourier Transform (FFT)
Y = fft(X);

% Compute the two-sided spectrum and then shift to the single-sided spectrum
P2 = abs(Y/L);
P1 = P2(1:L/2+1);
P1(2:end-1) = 2*P1(2:end-1);

% Define the frequency domain f
f = Fs*(0:(L/2))/L;

% Plotting all adjustments

% Plot the sine wave with harmonics
subplot(4,1,1);
plot(t(1:200), X(1:200))

title('Sine Wave with Harmonics')
xlabel('Time (s)')
ylabel('Amplitude')


%quantized
subplot(4,1,2);
stairs(t(1:200), X_quantized(1:200))

title('Sine Wave with Harmonics Quantized')
xlabel('Time (s)')
ylabel('Amplitude')


% Plot the single-sided amplitude spectrum of the signal with harmonics.
subplot(4,1,3);
plot(f, P1)
title('Single-Sided Amplitude Spectrum of Sine Wave with Harmonics')
xlabel('Frequency (Hz)')
ylabel('|P1(f)|')

% Plot the power spectral density
subplot(4,1,4);
psd = P1.^2/(Fs/L);
plot(f, 10*log10(psd))
title('Power Spectral Density of Sine Wave with Harmonics')
xlabel('Frequency (Hz)')
ylabel('Power/Frequency (dB/Hz)')
