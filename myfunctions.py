def horizontal_line(width):
    print('*' * width)
def vertical_line(shift, height):
    for i in range(0, height):
        print(' ' * shift + '*')
def two_vertical_lines(height, width):
    for i in range(0, height):
        print('*' + ' ' * (width - 2) + '*')
def number_0(width):
    for i in range(0, 5):
        if i in [0, 4]:
            horizontal_line(width)
        else:
            two_vertical_lines(1, width)
def number_1(width):
    vertical_line(width - 1, 5)
def number_2(width):
    for i in range(0, 5):
        if i in [0, 2, 4]:
            horizontal_line(width)
        elif i == 1:
            vertical_line(width - 1, 1)
        else:
            vertical_line(0, 1)
def number_3(width):
    for i in range(0, 5):
        if i in [0, 2, 4]:
            horizontal_line(width)
        else:
            vertical_line(width - 1, 1)
def number_4(width):
    for i in range(0, 5):
        if i == 2:
            horizontal_line(width)
        elif i in [0, 1]:
            two_vertical_lines(1, width)
        else:
            vertical_line(width - 1, 1)   
def number_5(width):
    for i in range(0, 5):
        if i in [0, 2, 4]:
            horizontal_line(width)
        elif i == 3:
            vertical_line(width - 1, 1)
        else:
            vertical_line(0, 1)
def number_6(width):
    for i in range(0, 5):
        if i in [0, 2, 4]:
            horizontal_line(width)
        elif i == 3:
            two_vertical_lines(1, width)
        else:
            vertical_line(0, 1)    
def number_7(width):
    for i in range(0, 5):
        if i in [0]:
            horizontal_line(width)
        else:
            vertical_line(width - 1, 1)    
def number_8(width):
    for i in range(0, 5):
        if i in [0, 2, 4]:
            horizontal_line(width)
        else:
            two_vertical_lines(1, width)
def number_9(width):
    for i in range(0, 5):
        if i in [0, 2]:
            horizontal_line(width)
        elif i == 1:
            two_vertical_lines(1, width)
        else:
            vertical_line(width - 1, 1)   
def plus(size):
    mid = int((size + 1) / 2)
    sp = ' ' * (mid - 1)
    for i in range(1, size + 1):
        if i != mid:
            print(sp + '*')
        else:
            print('*' * size)
def minus(size):
    for i in range(0, 5):
        if i == 2:
            horizontal_line(size)
        else:
            print()
def check_answer(x, y, z, cr):
    if (cr == '+' and x + y == z) or (cr == '-' and x - y == z):
        return True
    return False