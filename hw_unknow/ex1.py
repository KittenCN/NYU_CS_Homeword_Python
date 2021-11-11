num1 = int(input("Number 1:"))
while num1 < 0:
    print("Invalid, Try again")
    num1 = int(input("Number 1:"))
num2 = int(input("Number 2:"))
while num2 < 0 or num2 <= num1:
    print("Invalid, Try again")
    num2 = int(input("Number 2:"))
for i in range(num1, num2 + 1):
    line = str(i) + ' '
    for j in range(1, i + 1):
        line = line + '*'
    print(line)
for i in range(num2 - 1, num1 - 1, -1):
    line = str(i) + ' '
    for j in range(1, i + 1):
        line = line + '*'
    print(line)
