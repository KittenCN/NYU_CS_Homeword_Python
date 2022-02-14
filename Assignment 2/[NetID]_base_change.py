
"""Obtaining number representations in different bases


Write a program that asks for a natural number and a base and prints a representation of the number in the base provided: use a string for this
purpose. 
Prepared by
Mauricio Arias
"""
def base_change(num, base):
    if num == 0:
        return "0"
    if num < 0:
        return "-" + base_change(-num, base)
    result = ""
    while num > 0:
        num, remainder = divmod(num, base)
        result = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"[remainder] + result
    return result
x = int(input("What number are you inerested in converting?: "))
y = int(input("What base shall I use?: "))
while y < 2 or y > 9:
    print("The base has to be between 2 and 9. Please try again. \r\n")
    y = int(input("What base shall I use?: "))
print("The number {0} is represented by {1} in base {2}.".format(x, base_change(x, y), y))