stnum = int(input("Start number: "))
ennum = int(input("End number: "))
while stnum <= 0 or ennum <= 0:
    print("Start and end must be positive")
    stnum = int(input("Start number: "))
    ennum = int(input("End number: "))
while ennum <= stnum:
    print("End number must be greater than start number")
    stnum = int(input("Start number: "))
    ennum = int(input("End number: "))
for num in range(stnum, ennum + 1):
    prime_flag = True
    for i in range(2, num):
        if num % i == 0:
            prime_flag = False
            break
    if prime_flag is True:
        print(num)