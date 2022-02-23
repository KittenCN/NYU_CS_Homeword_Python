st = input("Enter a string: ")
for i in range(len(st)):
    print(st[i])
for i in range(len(st) - 1, -1, -1):
    print(st[i], end='')