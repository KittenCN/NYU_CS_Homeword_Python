import myfunctions
import random
cnt = int(input("How many problems woule you like to attempt?"))
while cnt <= 0:
    print("Invalid number, try again")
    print()
    cnt = int(input("How many problems woule you like to attempt?"))
size = int(input("How wide do you want your digits to be? 5-10"))
while size < 5 or size > 10:
    print("Invalid number, try again")
    print()
    size = int(input("How wide do you want your digits to be? 5-10"))
print("Here we go!")
scnt = 0
for i in range(0, cnt):
    print()
    print("What is . . .")
    print()
    x = random.randint(0, 9)
    y = random.randint(0, 9)
    cr = random.randint(0, 1)
    funx = "myfunctions.number_" + str(x) + "(" + str(size) + ")"
    funy = "myfunctions.number_" + str(y) + "(" + str(size) + ")"
    funcr = "myfunctions.plus" + "(" + str(size) + ")" if cr == 0 else "myfunctions.minus" + "(" + str(size) + ")"
    eval(funx)
    print()
    eval(funcr)
    print()
    eval(funy)
    print()
    ans = int(input("="))
    if myfunctions.check_answer(x, y, ans, "+" if cr == 0 else "-") is True:
        print("Corrent!")
        scnt += 1
    else:
        print("Sorry, that's not correct.")
print("You got " + str(scnt) + " out of " + str(cnt) + " corrent!")