import turtle
import time
import random
import math
from decimal import Decimal

num = int(input("Number of throws: "))
while num <= 0:
    print("Invalid, try again")
    num = int(input("Number of throws: "))
tur = input("Would you like to draw your results using turtle graphice? (yes/no): ")
while tur != "yes" and tur != "no":
    print("Invalid, try again")
    tur = input("Would you like to draw your results using turtle graphice? (yes/no): ")
if tur == "yes":
    length = 800
    height = 500
    turtle.setup(length, height)
    turtle.setworldcoordinates(0, height, length, 0)
    turtle.tracer(0)
    turtle.up()
    turtle.goto(0, 0)
    color = ["white", "black", "red", "yellow", "green", "blue","grey"]
    turtle.bgcolor(color[0])
    turtle.speed("fastest")
    turtle.hideturtle()
redcnt = 0
greencnt = 0
bluecnt = 0
greycnt = 0
yellowcnt = 0
missescnt = 0
sumcnt = 0
t1 = time.time()
while num > 0:
    mx = random.uniform(0, 800)
    my = random.uniform(0, 600)
    d1 = math.sqrt(math.pow((mx - 400), 2) + math.pow((my - 150), 2))
    d2 = math.sqrt(math.pow((mx - 400), 2) + math.pow((my - 300), 2))
    sumcnt += 1
    if tur == "yes":
        st = 5
        turtle.up()
        turtle.update()
        #turtle.exitonclick() 
    if mx >= 50 and mx <= 200 and my >= 100 and my <= 450:
        if tur == "yes":
            turtle.goto(mx, my)
            turtle.down()
            turtle.color(color[2])
            turtle.seth(90)
            while mx >= 50 and mx <= 200 and st > 0:
                turtle.forward(1)
                st -= 1
        redcnt += 1
    elif (((mx >= 600 and mx <= 650) or (mx >= 700 and mx <= 750)) and (my >= 50 and my <= 400)) or ((mx >= 650 and mx <= 700) and (my >= 350 and my <= 400)):
        if tur == "yes":
            turtle.goto(mx, my)
            turtle.down()
            turtle.color(color[3])
            turtle.seth(90)
            while (mx >= 600 and mx <= 750) and st > 0:
                turtle.forward(1)
                st -= 1        
        yellowcnt += 1
    elif d1 <= 100 and d2 > 100:
        if tur == "yes":
            turtle.goto(mx, my)
            turtle.down()
            turtle.color(color[4])
            turtle.seth(90)
            while d1 <= 100 and d2 > 100 and st > 0:
                d1 = math.sqrt(math.pow((turtle.xcor() - 400), 2) + math.pow((turtle.ycor() - 150), 2))
                d2 = math.sqrt(math.pow((turtle.xcor() - 400), 2) + math.pow((turtle.ycor() - 300), 2))
                turtle.forward(1)
                st -= 1        
        greencnt += 1
    elif d2 <= 100 and d1 > 100:
        if tur == "yes":
            turtle.goto(mx, my)
            turtle.down()
            turtle.color(color[5])
            turtle.seth(90)
            while d2 <= 100 and d1 > 100 and st > 0:
                d1 = math.sqrt(math.pow((turtle.xcor() - 400), 2) + math.pow((turtle.ycor() - 150), 2))
                d2 = math.sqrt(math.pow((turtle.xcor() - 400), 2) + math.pow((turtle.ycor() - 300), 2))
                turtle.forward(1)
                st -= 1   
        bluecnt += 1
    elif d2 <= 100 and d1 <= 100:
        if tur == "yes":
            turtle.goto(mx, my)
            turtle.down()
            turtle.color(color[6])
            turtle.seth(90)
            while d2 <= 100 and d1 <= 100 and st > 0:
                d1 = math.sqrt(math.pow((turtle.xcor() - 400), 2) + math.pow((turtle.ycor() - 150), 2))
                d2 = math.sqrt(math.pow((turtle.xcor() - 400), 2) + math.pow((turtle.ycor() - 300), 2))
                turtle.forward(1)
                st -= 1  
        greycnt += 1
    else:
        missescnt += 1
    num -= 1
t2 = time.time()
tt = t2 - t1
print()
print("Total time elapsed: " + str(Decimal(round(tt, 4)).quantize(Decimal("0.00"))) + " seconds")
print("Red" + " " * 10 + str(redcnt) + " (" + str(Decimal(round(redcnt / sumcnt, 4) * 100.0).quantize(Decimal("0.00"))) + "%)")
print("Green" + " " * 10 + str(greencnt) + " (" + str(Decimal(round(greencnt / sumcnt, 4) * 100.0).quantize(Decimal("0.00"))) + "%)")
print("Blue" + " " * 10 + str(bluecnt) + " (" + str(Decimal(round(bluecnt / sumcnt, 4) * 100.0).quantize(Decimal("0.00"))) + "%)")
print("Grey" + " " * 10 + str(greycnt) + " (" + str(Decimal(round(greycnt / sumcnt, 4) * 100.0).quantize(Decimal("0.00"))) + "%)")
print("Yellow" + " " * 10 + str(yellowcnt) + " (" + str(Decimal(round(yellowcnt / sumcnt, 4) * 100.0).quantize(Decimal("0.00"))) + "%)")
print("Misses" + " " * 10 + str(missescnt) + " (" + str(Decimal(round(missescnt / sumcnt, 4) * 100.0).quantize(Decimal("0.00"))) + "%)")
if tur == "yes":
    turtle.exitonclick() 
