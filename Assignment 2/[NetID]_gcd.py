"""The Greatest Common Divisor


Write a program that asks for two numbers and calculates the
greatest common divisor using the Euclidean algorithm. 
Prepared by
Mauricio Arias
"""
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
x = int(input("What is the first number?: "))
y = int(input("What is the second number?: "))
print("gcd({0}, {1}) = {2}".format(x, y, gcd(x, y)))