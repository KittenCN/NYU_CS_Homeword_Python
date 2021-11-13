money = float(input())
maxcur = 0
for i in range(12):
    tmp = float(input())
    if tmp > maxcur:
        maxcur = tmp
print(round(money * maxcur, 2))