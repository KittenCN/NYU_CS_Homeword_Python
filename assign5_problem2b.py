num = 2
print("1 is technically not a prime number.")
while num <= 1000:
    prime_flag = True
    for i in range(2, num):
        if num % i == 0:
            prime_flag = False
            break
    if prime_flag is True:
        print(str(num) + " is a prime number!")
    num += 1