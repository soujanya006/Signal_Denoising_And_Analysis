% Parameters for the sine wave
Fs = 1000;             % Sampling frequency in Hz
T = 1/Fs;              % Sampling period in seconds
L = 1500;              % Length of the signal (number of samples)
t = (0:L-1)*T;         % Time vector

f = 50;                % Frequency of the sine wave in Hz
A = 0.7;               % Amplitude of the sine wave

% Generate the fundamental sine wave
X = A * sin(2 * pi * f * t);

% Parameters for harmonics
numHarmonics = 3;      % Number of harmonics to add
harmonicPhaseShift = 0; % Systematic phase shift for alignment

% Adjusting the amplitude and phase shift for each harmonic
for n = 2:numHarmonics+1
    harmonicAmplitude = A / n; % Decreasing amplitude for each harmonic
    % Using a systematic phase shift to align peaks
    X = X + harmonicAmplitude * sin(2 * pi * f * n * t + harmonicPhaseShift);
end

% Plotting the sine wave with harmonics
figure;
plot(t(1:200), X(1:200));
title('Sine Wave with Decreasing Strength Harmonics');
xlabel('Time (s)');
ylabel('Amplitude');
