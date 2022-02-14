"""Template script to make WAV files


This script creates a simple WAV file that produces alternating tones
at predetermined frequencies. It runs for a user-defined number of
seconds.
Prepared by
Mauricio Arias
"""
import math
from Lib.WAV_utilities import *
filename = "[NetID]_alternating_tones.wav"
sound_file = open(filename, 'wb')
freq1_in_Hz = A_freq * 2 
freq2_in_Hz = A_freq
channels = 1
samples_per_s = 8000 
time_between_samples = 1 / samples_per_s
duration_in_s = int(input("Enter duration in seconds: "))
sound_binary = header(duration_in_s, samples_per_s, channels)
print()
time_elapsed = 0
sample_number = 0
total_samples = duration_in_s * samples_per_s
while sample_number < total_samples:
   freq = freq1_in_Hz if time_elapsed // 0.25 % 2 == 0 else freq2_in_Hz
   sample = max_amplitude / 10 * math.sin(2 * math.pi * freq * time_elapsed)
   encoded_sample = bytes_pack_signed(int(sample), sample_depth//8)
   sound_binary += encoded_sample
   sample_number += 1
   time_elapsed += time_between_samples
print(f"File Size is {len(sound_binary)}")
sound_file.write(sound_binary)
sound_file.close()
print(f"{filename} WAV file was generated...")
