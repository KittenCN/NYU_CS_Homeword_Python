num = int(input("Enter a positive number to test: "))
while num <= 0:
    print("Invalid number, try again")
    num = int(input("Enter a positive number to test: "))
prime_flag = True
for i in range(2, num):
    if num % i == 0:
        print(str(i) + " is a divisor of " + str(num) + " ... stopping")
        prime_flag = False
        break
    else:
        print(str(i) + " is NOT a divisor of " + str(num) + " ... continuing")
if prime_flag is True:
    print(str(num) + " is a prime number!")
else:
    print(str(num) + " is not a prime number.")