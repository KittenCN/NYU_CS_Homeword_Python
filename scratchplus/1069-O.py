import math
for i in range(10,1000000):
    tmp = 0
    n = i
    while n > 0:
        tmp = (tmp * 10) + (n % 10)
        n = int(n / 10)
    stmp = int(math.sqrt(i))
    if stmp * stmp == i and tmp == i:
        print(i)