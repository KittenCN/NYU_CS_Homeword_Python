for x in range (1,100):
  for y in range(1,100):
    z = 100 - x -y
    if(5*x + 3*y + z/3 == 100) and z%3 ==0:
        print(x,y,z)