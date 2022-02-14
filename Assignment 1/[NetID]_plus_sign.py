"""This program makes a BMP file with a plus sign of a specified color
Submitted by Mauricio Arias, NetID ma6918
"""
from turtle import width
import utilities_BMP as bmp
import colors_BMP as colors

filename = "my_other.bmp"
picture_file = open(filename,'wb')

height = int(input("Enter the length of the square: "))
width = int(input("Enter the width of the square: "))
if width % 4 != 0:
    width += 4 - (width % 4)
thickness = int(input("Enter the thickness of the square: "))

image_binary = bmp.header(width, height, colors.bytes_per_pix)
background_color = colors.dim_grey_pix
sign_color = colors.steel_blue_pix

for i in range(int((height - thickness) / 2)):
    image_binary += background_color * int((width - thickness) / 2)
    image_binary += sign_color * thickness
    image_binary += background_color * int((width - thickness) / 2)
image_binary += sign_color * thickness * width
for i in range(int((height - thickness) / 2)):
    image_binary += background_color * int((width - thickness) / 2)
    image_binary += sign_color * thickness
    image_binary += background_color * int((width - thickness) / 2)

print(f"The actual file size is {len(image_binary)}.")
picture_file.write(image_binary)
picture_file.close()