from turtle import width
import Lib.utilities_BMP as bmp
import Lib.colors_BMP as colors

filename = "my_other.bmp"
picture_file = open(filename,'wb')

cellh = int(input("Enter the length of the cells: ") or "50") 
if cellh < 1 or cellh > 200:
    print("Invalid input.")
    exit()
cells = int(input("Enter the number of cells: ") or "8")
if cells < 1 or cells > 200:
    print("Invalid input.")
    exit()
if cellh * cells > 2000:
    print("The image is too large to be saved in a BMP file.")
    exit()
cellw = cellh
edge_size = cellh * cells // 80
height = cellh * cells + (2 * edge_size)
fit = 0
if height % 4 != 0:
    fit = 4 - (height % 4)
    height += 4 - (height % 4)
edge_size += fit // 2
width = height
image_binary = bmp.header(width, height, colors.bytes_per_pix)
odd_color = colors.brown_pix
even_color = colors.coral_pix
edge_color = colors.black_pix

image_binary += edge_color * width * edge_size
for i in range(1, cells + 1):
    for j in range(1, cellh + 1):
        image_binary += edge_color * edge_size
        for k in range(1, cells + 1):
            if (i % 2 ==1 and k % 2 == 1) or (i % 2 ==0 and k % 2 == 0):
                image_binary += even_color * cellw
            elif (i % 2 ==1 and k % 2 == 0) or (i % 2 ==0 and k % 2 == 1):
                image_binary += odd_color * cellw
        image_binary += edge_color * edge_size
image_binary += edge_color * width * edge_size
picture_file.write(image_binary)
picture_file.close()