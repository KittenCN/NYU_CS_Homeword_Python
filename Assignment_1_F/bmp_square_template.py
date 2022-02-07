"""This program draws a square in a BMP file using specified colors"""


import utilities_BMP as bmp
import colors_BMP as colors

filename = "my_bitmap.bmp"
picture_file = open(filename,'wb')

# Size information for the image
# TODO: Ask for the size of the square.
# size_width and size_height are the same. Use square_length for the
# variable name.

square_length = 400

# Header with information about the size of the file.
image_binary = bmp.header(square_length, square_length, colors.bytes_per_pix)

# TODO: write the code to fill the data section in the space below
# Pixel by pixel color information starting from the bottom up and left
# to right. All rows are padded to a multiple of 4. Concatenate the
# padding byte in bmp.pad_byte as many times as needed as described
# in the assignment instructions.
#
# For each pixel, colors are specified as follows: Blue channel, Green
# channel & then Red channel. Many colors are already defined in the
# BMP_colors.py module. Open that file to learn what is available. For
# example write colors.salmon_pix in your code to use the salmon color.
#
# A formula for the number of bytes to add is
# (4 - square_length * colors.bytes_per_pix % 4) % 4
# Make sure you understand it.
# Below we use an equivalent one that takes advantage of how
# the % operator works with negative numbers.

padding = bmp.pad_byte * (-square_length * colors.bytes_per_pix % 4)
border_color = colors.salmon_pix
inner_color = colors.powder_blue_pix





# Do not edit after this point
print(f"The actual file size is {len(image_binary)}.")
picture_file.write(image_binary)
picture_file.close()