"""Utilities for generating the header of bitmap files.


Useful parameters are included as well as the main header composition function
"""

pad_byte = bytearray(b'\x00')


def header(width, height, color_depth):
    # Header information about the size of the file.
    # Only 4 bytes are allotted. The maximum file size is then 14**(2x4)-1.
    # This corresponds to images smaller than 65536 * 65536.
    size_w = width
    size_l = height

    # Initial Code for BMP files
    file_header = bytearray(b'\x42\x4D')

    # For the size a padding correction is included by adding 3 to the width in
    # bytes and dividing by 4: equiv to ceiling.
    image_total_bytes = size_l * (size_w * color_depth +
                                  -size_w * color_depth % 4)
    print(f"The expected image size is {image_total_bytes}.")
    total_bytes = image_total_bytes + 54
    print(f"The expected file size is {total_bytes}.")
    left_over = total_bytes
    for spaces in range(0, 4):
        file_header.append(left_over % 256)
        left_over //= 256

    # Adding 4 unused bytes
    for unused_bytes in range(0, 4):
        file_header.append(0)

    # Offset. For this application it is constant at 54
    file_header.append(54)
    for extra_spaces in range(0, 3):
        file_header.append(0)

    # Size of the DIB header. For this application it is constant at 40
    file_header.append(40)
    for extra_spaces in range(0, 3):
        file_header.append(0)

    # Size of the picture width (size_w) x height (size_l)
    left_over = size_w
    for spaces in range(0, 4):
        file_header.append(left_over % 256)
        left_over //= 256
    left_over = size_l
    for spaces in range(0, 4):
        file_header.append(left_over % 256)
        left_over //= 256

    # Number of planes. In this case, constant at 1
    file_header.append(1)
    for extra_spaces in range(0, 1):
        file_header.append(0)

    # Number of bits per pixel
    file_header.append(24)
    for extra_spaces in range(0, 1):
        file_header.append(0)

    # Unused bytes in this application
    for extra_spaces in range(0, 4):
        file_header.append(0)

    # Size of image data per se
    left_over = image_total_bytes
    for spaces in range(0, 4):
        file_header.append(left_over % 256)
        left_over //= 256

    # Resolution: 72 DPI * 39.3701 rounds up to 2835
    for axis in ["w", "l"]:
        resolution = 2835
        left_over = resolution
        for spaces in range(0, 4):
            file_header.append(left_over % 256)
            left_over //= 256

    # Colors in palette: 0. Functionality not used
    for extra_spaces in range(0, 4):
        file_header.append(0)

    # Important colors in palette: 0. 0 means all are important
    for extra_spaces in range(0, 4):
        file_header.append(0)

    return file_header
