num = int(input("Enter a positive integer:"))
nums = num
maxnum = -1
m1 = 7
m2 = 7
m3 = 9
m4 = 11
li1 = []
li2 = []
li3 = []
li4 = []
while num < 1:
    print("Number must be positive, try again.")
    num = int(input("Enter a positive integer:"))
mo = input("Silent mode? (yes/no): ")
while mo != "yes" and mo != "no":
    print("Invalid option, try again.")
    mo = input("Silent mode? (yes/no): ")

cnt = 0
while num > 1:
    cnt += 1
    if num % 2 == 0:
        li1.append(str(cnt))
        m1 = max(m1, len(str(int(cnt))))
        li2.append(str(int(num)))
        m2 = max(m2, len(str(int(num))))
        li3.append("even")
        m3 = max(m3, len("even"))
        li4.append(str(int(num)) + " / 2 = " + str(int(num / 2)))
        m4 = max(m4, len(str(int(num)) + " / 2 = " + str(int(num / 2))))
        num /= 2
    elif num % 2 == 1:
        li1.append(str(cnt))
        m1 = max(m1, len(str(int(cnt))))
        li2.append(str(int(num)))
        m2 = max(m2, len(str(int(num))))
        li3.append("odd")
        m3 = max(m3, len("odd"))
        li4.append(str(int(num)) + " * 3 + 1 = " + str(int(num * 3 + 1)))
        m4 = max(m4, len(str(int(num)) + " * 3 + 1 = " + str(int(num * 3 + 1))))
        num = num * 3 + 1
    if num > maxnum:
        maxnum = num
if mo == "no":
    print("Period" + " " * (m1 - 6) + "Number" + " " * (m2 - 6) + "Even/Odd" + " " * (m3 - 8) + "Expression" + " " * (m4 - 10))
    for i in range(0, cnt):
        print(str(li1[i]) + " " * (m1 - len(str(li1[i]))) + str(li2[i]) + " " * (m2 - len(str(li2[i]))) + str(li3[i]) + " " * (m3 - len(str(li3[i]))) + str(li4[i]) + " " * (m4 - len(str(li4[i]))))
    cnt += 1
    print(str(cnt) + " " * (m1 - len(str(li1[i]))) + "1" + " " * (m2 - len(str(li2[i]))) + "odd" + " " * (m3 - len(str(li3[i])) + 1) + "1 * 3 + 1 = 4" + " " * (m4 - len(str(li4[i]))))
    print()
    print("Period for " + str(int(nums)) + ": " + str(int(cnt)))
    print("Highest numer reached:" + str(int(maxnum)))
else:
    print()
    cnt += 1
    print("Period for " + str(int(nums)) + ": " + str(int(cnt)))
    print("Highest numer reached:" + str(int(maxnum)))