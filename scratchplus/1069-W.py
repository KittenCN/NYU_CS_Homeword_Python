import math
n = int(input())
cnt = 0
for i in range(n):
    sum = 0
    for j in range(1, int(math.sqrt(i)) + 1):
        if i % j == 0:
            sum += j
            if i // j != j and j != 1:
                sum += i // j
    sumt = 0
    for j in range(1, int(math.sqrt(sum)) + 1):
        if sum % j == 0:
            sumt += j
            if sum // j != j and j != 1:
                sumt += sum // j
    if i == sumt and i != sum and i < sum:
        print(str(i) + " " + str(sum))
        cnt += 1
if cnt == 0:
    print("nothing")