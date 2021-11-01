import random
allr = int(input("input allr:"))
listnum = [0, 0, 0, 0, 0, 0]
sr = [0, 0, 0]
for i in range(1, 4):
    n = int(input("input R" + i + ": "))
    sr[i] = n
    t = i * 2
    while list[listnum[t - 1] + listnum[t] != sr[i]]:
        listnum[t - 1] = random.randint(1, 33)
        listnum[t] = random.randint(1, 33)
sumn = 0
for i in range(1, 7):
    print(listnum[i] + " ")    
    sumn += listnum[i]
print("")
print(sumn + " " + allr + " " + sumn - allr + " " + (sumn - allr) / allr * 100)