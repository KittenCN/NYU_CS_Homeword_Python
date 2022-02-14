"""This program makes a BMP file with a plus sign of a specified color
Submitted by Mauricio Arias, NetID ma6918
"""
import utilities_BMP as bmp
import colors_BMP as colors

filename = "my_bitmap.bmp"
picture_file = open(filename,'wb')

square_length = int(input("Enter the length of the square: "))
if square_length % 4 != 0:
    square_length += 4 - (square_length % 4)
top_length = 5
image_binary = bmp.header(square_length, square_length, colors.bytes_per_pix)
square_padding = bmp.pad_byte * (-square_length * colors.bytes_per_pix % 4)
border_color = colors.salmon_pix
inner_color = colors.powder_blue_pix
image_binary += border_color * top_length * square_length
for i in range(square_length - top_length * 2):
    image_binary += border_color * top_length
    image_binary += inner_color * (square_length - top_length * 2)
    image_binary += border_color * top_length
image_binary += border_color * top_length * square_length

print(f"The actual file size is {len(image_binary)}.")
picture_file.write(image_binary)
picture_file.close()