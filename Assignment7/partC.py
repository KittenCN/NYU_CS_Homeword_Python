import turtle
secret = ['penup', '', '', 'goto', -201, 145, 'pendown', -201, 145, 'color', 'black', 'yellow', 'goto', -158, 145, 'goto', -97, 126, 'goto', -53, 141, 'goto', 13, 132, 'goto', 52, 192, 'goto', 94, 221, 'goto', 96, 162, 'goto', 41, 99, 'goto', 58, 65, 'goto', 51, -2, 'goto', 61, -46, 'goto', 82, -104, 'goto', 83, -164, 'goto', 66, -191, 'goto', 75, -227, 'goto', 69, -240, 'goto', 44, -226, 'goto', 26, -197, 'goto', -44, -194, 'goto', -68, -199, 'goto', -98, -222, 'goto', -132, -227, 'goto', -109, -190, 'goto', -129, -150, 'goto', -119, -81, 'goto', -111, -30, 'goto', -141, 4, 'goto', -148, 24, 'goto', -135, 60, 'goto', -120, 100, 'goto', -156, 101, 'goto', -184, 108, 'stop_color', '', '', 'goto', -201, 145, 'penup', '', '', 'goto', -201, 145, 'pendown', -201, 145, 'color', 'black', 'black', 'goto', -245, 141, 'goto', -185, 106, 'stop_color', '', '', 'goto', -201, 145, 'penup', '', '', 'goto', 92, 220, 'pendown', 92, 220, 'color', 'black', 'black', 'goto', 132, 248, 'goto', 122, 202, 'goto', 95, 161, 'stop_color', '', '', 'goto', 92, 220, 'penup', '', '', 'goto', 82, -126, 'pendown', 82, -126, 'color', 'black', 'yellow', 'goto', 121, -90, 'goto', 75, -64, 'goto', 103, -23, 'goto', 55, -7, 'goto', 61, 66, 'goto', 116, 128, 'goto', 206, 70, 'goto', 132, 6, 'goto', 194, -25, 'goto', 135, -62, 'goto', 177, -88, 'goto', 83, -152, 'stop_color', '', '', 'goto', 82, -126, 'penup', '', '', 'goto', -116, 78, 'pendown', -116, 78, 'color', 'black', 'black', 'goto', -122, 63, 'goto', -118, 52, 'goto', -104, 51, 'goto', -97, 64, 'goto', -104, 81, 'stop_color', '', '', 'goto', -116, 78, 'penup', '', '', 'goto', -26, 82, 'pendown', -26, 82, 'color', 'black', 'black', 'goto', -36, 69, 'goto', -28, 52, 'goto', -9, 50, 'goto', 1, 65, 'goto', -6, 82, 'stop_color', '', '', 'goto', -26, 82, 'penup', '', '', 'goto', 10, 42, 'pendown', 10, 42, 'color', 'black', 'orange', 'goto', -8, 37, 'goto', -9, 18, 'goto', 0, 11, 'goto', 22, 10, 'goto', 27, 29, 'stop_color', '', '', 'goto', 10, 42, 'penup', '', '', 'goto', -140, 36, 'pendown', -140, 36, 'color', 'black', 'orange', 'goto', -130, 27, 'goto', -140, 0, 'goto', -149, 22, 'stop_color', '', '', 'goto', -140, 36, 'penup', '', '', 'goto', -86, 40, 'pendown', -86, 40, 'color', 'black', 'black', 'goto', -80, 51, 'goto', -75, 40, 'stop_color', '', '', 'goto', -86, 40, 'penup', '', '', 'goto', -98, 30, 'pendown', -98, 30, 'color', 'black', 'black', 'goto', -90, 24, 'goto', -81, 27, 'goto', -73, 23, 'goto', -61, 26, 'goto', -57, 19, 'goto', -71, 16, 'goto', -81, 21, 'goto', -93, 18, 'goto', -103, 25, 'stop_color', '', '', 'goto', -98, 30, 'penup', '', '']
length = 500
height = 500
turtle.setup(length, height)
turtle.tracer(0)
turtle.up()
turtle.goto(0, 0)
turtle.speed("fastest")
for i in range(len(secret)):
    if secret[i] == 'goto':
        turtle.goto(secret[i + 1], secret[i + 2])
    elif secret[i] == 'penup':
        turtle.penup()
    elif secret[i] == 'pendown':
        turtle.pendown()
    elif secret[i] == 'color':
        turtle.pencolor(secret[i + 1])
        turtle.fillcolor(secret[i + 2])
        turtle.begin_fill()
    elif secret[i] == 'stop_color':
        turtle.end_fill()
    turtle.update()
turtle.exitonclick()