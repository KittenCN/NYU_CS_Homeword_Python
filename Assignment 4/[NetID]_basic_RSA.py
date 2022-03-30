from NetID_utilities_RSA import raise_mod, gcd
file_add = "Assignment 4/large prime numbers.txt"
import math
import random

def get_(a, b):
	if b == 0:
		return 1, 0
	else:
		k = a // b		
		x1, y1 = get_(b, a % b)
		x, y = y1, (x1 - k * y1)
	return x,y

if __name__ == '__main__':
    file = open(file_add, "r")
    arrfile = []
    for line in file:
        arrfile.append(line.strip().split('	'))
    file.close()
    for i in range(len(arrfile)):
        for j in range(len(arrfile[i])):
            print(arrfile[i][j],end=" ")
        print('\n')
    print("\n")
    p = int(input("Enter the 1st prime number: "))
    q = int(input("Enter the 2nd prime number: "))
    n = p*q
    fn = (p-1)*(q-1)

    while True:
        key1 = random.randint(2**64,2**65)
        if  gcd(fn, key1):
            break
    k, key2 = get_(fn,key1)
    if key2<0: 
        key2 = key2 % fn
    m = int(input("Enter the Numer:"))
    c = raise_mod(m,key1,n)
    print("encrypt：",c)
    m = raise_mod(c,key2,n)
    print("decrypt:",m)
