import random
from decimal import Decimal
print("Jelly Bean Jar Simulator")
st = input("Pick a color! (R)ed, (O)range, (Y)ellow, (G)reen, (B)lue, (I)ndigo or (V)iolet:")
colist1 = ['R','O','Y','G','B','I','V']
while len(st) != 1 or (st[0] not in colist1 and st[0].swapcase() not in colist1):
    print("Invalid select, try again")
    st = input("Pick a color! (R)ed, (O)range, (Y)ellow, (G)reen, (B)lue, (I)ndigo or (V)iolet:")
print("Thanks, here we go!")
num1 = 0
num2 = 0
cnt = 0
cntDou = 0
cntNei = 0
cntRV = 0
flag = 0
while flag == 0 or (num1 != num2 or (colist1[num1] != st[0] and colist1[num1] != st[0].swapcase())):
    num1 = random.randint(0,6)
    num2 = random.randint(0,6)
    flag = 1
    cnt += 1
    line = str(cnt) + ". " + colist1[num1] + " and " + colist1[num2]
    if num1 == num2 and (colist1[num1] != st[0] and colist1[num1] != st[0].swapcase()):
        line += " doubles!"
        cntDou += 1
    elif abs(num1 - num2) == 1:
        line += " neighbors!"
        cntNei += 1
    elif num1 == 0 and num2 == 6:
        line += " first & last!"
        cntRV += 1
    elif num1 == num2 and (colist1[num1] == st[0] or colist1[num1] == st[0].swapcase()):
        line += " doubles! your bean came out twice!"
    print(line)
print()
print("Total picks:" + str(cnt))
print("Doubles:" + str(cntDou) + '(' + str(Decimal(round(cntDou / cnt,4) * 100.0).quantize(Decimal("0.00"))) + "%)")
print("Neighbors:" + str(cntNei) + '(' + str(Decimal(round(cntNei / cnt,4) * 100.0).quantize(Decimal("0.00"))) + "%)")
print("First/Last:" + str(cntRV) + '(' + str(Decimal(round(cntRV / cnt,4) * 100.0).quantize(Decimal("0.00"))) + "%)")
