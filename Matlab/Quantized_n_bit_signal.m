% Simple sinusoidal signal parameters
Fs = 1000; % Sampling frequency in Hz
T = 1/Fs; % Sampling period in seconds
L = 1500; % Length of the signal
t = (0:L-1)*T; % Time vector

% Generate a simple sinusoidal signal
f = 50; % Frequency of the sine wave in Hz
A = 1; % Amplitude of the sine wave
X = A * sin(2 * pi * f * t); % Sinusoidal signal

% Quantization parameters
n = 2;
L_quant = 2^n - 1;

% Quantize the signal
X_min = min(X);
X_max = max(X);
Delta = (X_max - X_min) / L_quant;
X_quantized = round((X - X_min) / Delta) * Delta + X_min;

% Plotting the original and quantized signals
figure;
subplot(2,1,1);
stairs(t(1:200), X(1:200));
title('Original Sinusoidal Signal');
xlabel('Time (s)');
ylabel('Amplitude');

subplot(2,1,2);
stairs(t(1:200), X_quantized(1:200)); % Using 'stairs' for better visualization of quantization
title('Quantized Sinusoidal Signal');
xlabel('Time (s)');
ylabel('Amplitude');
