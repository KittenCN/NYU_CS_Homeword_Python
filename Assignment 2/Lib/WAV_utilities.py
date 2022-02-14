"""Utilities for making simple WAV files


Prepared by
Mauricio Arias
"""


import random

# The intensity of the sound is encoded in 3 bytes for each sample
sample_depth = 24  # 3 bytes
# Signed values limit max_amplitude we can represent to ~half
max_amplitude = 2**(sample_depth-1) - 1

# Some values for reference: notes A4 through G5 sharp
pause_freq = 0  # This generates silence (0 intensity)
A_freq = 440
# For the other notes equal temperament is used
A_sharp_freq = A_freq * 2 ** (1/12)
B_freq = A_freq * 2 ** (2/12)
C_freq = A_freq * 2 ** (3/12)
C_sharp_freq = A_freq * 2 ** (4/12)
D_freq = A_freq * 2 ** (5/12)
D_sharp_freq = A_freq * 2 ** (6/12)
E_freq = A_freq * 2 ** (7/12)
F_freq = A_freq * 2 ** (8/12)
F_sharp_freq = A_freq * 2 ** (9/12)
G_freq = A_freq * 2 ** (10/12)
G_sharp_freq = A_freq * 2 ** (11/12)

def bytes_pack_unsigned(unsigned_int, number_of_bytes):
    """Packs unsigned integers. Returns a bytearray as little endian"""
    left_over = unsigned_int
    encoded = bytearray(b'')
    for counter in range(number_of_bytes):
        encoded.append(left_over % 256)
        left_over //= 256
    return encoded


def bytes_pack_signed(signed_int, number_of_bytes):
    """Packs signed integers. Returns a bytearray as little endian.
    It trims number_of_bytes from (2**number_of_bytes + signed_int) as
    little endian. This generates the two's complement for the bytes of
    interest.
    """
    pre_trim = (1 << number_of_bytes * 8) + signed_int
    left_over = pre_trim
    encoded = bytearray(b'')
    for counter in range(number_of_bytes):
        encoded.append(left_over % 256)
        left_over //= 256
    return encoded

def sin(mock):
    """This function illustrates the problems of 'from [lib] import *'"""
    print("Check how you are invoking sin().\nProf. Arias")
    print()
    return random.random()


def header(total_time, sampling, channels):
    """Composes the header for a simple WAV file"""
    file_header = b'RIFF'
    header_size = 44  # By accounting for all the fields used

    # Insert the size in byte format: little-endian
    file_size = (header_size 
                 + int(total_time * sampling * channels) * (sample_depth//8))
    # print(f"Calculated file size: {file_size}")
    file_header += bytes_pack_unsigned(file_size, 4)

    # Starting the DATA section of the main packet
    file_header += b'WAVE'

    # Starting the Chunk section of the file
    file_header += b'fmt '

    # Insert the size of the chunk data size.
    chunk_data_size = 16
    file_header += bytes_pack_unsigned(chunk_data_size, 4)

    # Compression Code: 0->Unknown, 1->Uncompressed, 2->MS ADPCM, ...
    compression_code = 1  # Only canonical fields are used.
    file_header += bytes_pack_unsigned(compression_code, 2)

    # Number of channels
    number_of_channels = channels  # Up to two channels can be used.
    file_header += bytes_pack_unsigned(number_of_channels, 2)

    # Sample rate
    sample_rate = sampling  # Provided in function call
    file_header += bytes_pack_unsigned(sample_rate, 4)

    # Byte rate
    byte_rate = sampling * channels * (sample_depth//8)
    file_header += bytes_pack_unsigned(byte_rate, 4)

    # Block align. This is the aggregate for all channels
    block_align = number_of_channels * (sample_depth//8)
    file_header += bytes_pack_unsigned(block_align, 2)

    # Significant bits per sample
    significant_bits = sample_depth
    file_header += bytes_pack_unsigned(significant_bits, 2)

    # Entering the actual sound data
    file_header += b'data'

    sound_type = "mono" if channels == 1 else "stereo"
    # Insert the size in byte format: little-endian
    raw_sound_size = int(channels * sampling * total_time * (sample_depth//8))
    file_header += bytes_pack_unsigned(raw_sound_size, 4)

    print(f"Total header size: {len(file_header)}")
    print(f"Estimated size for the sound section: {raw_sound_size} bytes "
          f"(sampling {sampling}, duration {total_time} s, {sound_type})")

    return file_header
