size = int(input("Enter size for your pattern (3-9):"))
while size < 3 or size > 9:
    print("Invalid size, try again")
    size = int(input("Enter size for your pattern (3-9):"))
cr = str(input("Enter a single character for your pattern:"))
while len(cr) != 1:
    print("Invalid character, try again")
    cr = str(input("Enter a single character for your pattern:"))
line = ""
line1 = ""
print()
print("Pattern #1")
print()
line = str(cr[0]) * size
for i in range(1, size + 1):
    print(line)
print()
print("Pattern #2")
print()
line1 = str(cr[0]) + " " * (size - 2) + str(cr[0])
for i in range(1, size + 1):
    if i == 1 or i == size:
        print(line)
    else:
        print(line1)
print()
print("Pattern #3")
print()
line1 = " " * size + str(cr[0]) * size
for i in range(1, size + 1):
    if(i % 2 == 1):
        print(line)
    else:
        print(line1)
print()
print("Pattern #4")
print()
for i in range(1, size + 1):
    print(str(cr[0]) + str(i - 1) * size + str(cr[0]))
print()
print("Pattern #5")
print()
for i in range(size, 0, -1):
    print(" " * (i - 1) + line)
