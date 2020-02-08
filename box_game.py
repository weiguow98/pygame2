import turtle
import random
import time
speed = 0
if speed < 0 or speed > 10:
  raise Exception("Speed out of range! Please input a value between 0 and 10 (inclusive)")

window=turtle.Screen()
window.bgcolor("#444444")

image = "C:/Users/wan020336/Documents/Python/pygame/ghost.gif"
pacimage = "C:/Users/wan020336/Documents/Python/pygame/pacman.gif"

# add the shape first then set the turtle shape
window.addshape(image)
window.addshape(pacimage)
turtle.shape(image)
turtle.forward(310)
turtle.goto(310,100)
t2 = turtle.Turtle()
t2.shape(image)
t2.goto(30, -100)

outer=turtle.Turtle()
hello=turtle.Turtle()

grid=turtle.Turtle()

winner=turtle.Turtle()
xlist = [-245, -195, -145, -95, -45, 5, 55, 105, 155, 205, 255]
ylist = [-205, -155, -105, -55, -5, 45, 95, 145, 195, 245, 295]
gridpos = [-200, -150, -100, -50, 0, 50, 100, 150, 200]
playerposlist = [-225, -175, -125, -75, -25, 25, 75, 125, 175, 225]

box1x = box1y = box1gridx = box1gridy = 0
box2x = box2y = box2gridx = box2gridy = 0
box3x = box3y = box3gridx = box3gridy = 0
box4x = box4y = box4gridx = box4gridy = 0
box5x = box5y = box5gridx = box5gridy = 0
box6x = box6y = box6gridx = box6gridy = 0
box7x = box7y = box7gridx = box7gridy = 0



outer.ht()
hello.ht()


grid.ht()

winner.ht()

outer.speed(speed)
outer.color("#000000","#FFFFFF")
outer.up()
outer.goto(250,250)
outer.down()
outer.begin_fill()
for i in range(4):
  outer.rt(90)
  outer.fd(500)
outer.end_fill()

grid.speed(speed)
grid.color("#888888")
for a in range(9):
  grid.up()
  grid.goto(-250,gridpos[a])
  grid.down()
  grid.fd(500)
  grid.lt(90)
  grid.up()
  grid.goto(gridpos[a],-250)
  grid.down()
  grid.fd(500)
  grid.rt(90)

box1gridx = random.randint(0,9)
box1gridy = random.randint(0,9)
box1x = xlist[box1gridx]
box1y = ylist[box1gridy]
print("box1")
print(box1x,box1y)

while True:
  box2gridx = random.randint(0,9)
  box2gridy = random.randint(0,9)
  box2x = xlist[box2gridx]
  box2y = ylist[box2gridy]
  print(box2x,box2y)
  if (box2x == box1x and box2y == box1y):
    print("Box 2 placement failed, retrying...")
  else:
    break

while True:
  box3gridx = random.randint(0,9)
  box3gridy = random.randint(0,9)
  box3x = xlist[box3gridx]
  box3y = ylist[box3gridy]
  print(box3x,box3y)
  if (box3x == box1x and box3y == box1y) or (box3x == box2x and box3y == box2y):
    print("Box 3 placement failed, retrying...")
  else:
    break

while True:
  box4gridx = random.randint(0,9)
  box4gridy = random.randint(0,9)
  box4x = xlist[box4gridx]
  box4y = ylist[box4gridy]
  print(box4x,box4y)
  if (box4x == box1x and box4y == box1y) or (box4x == box2x and box4y == box2y) or (box4x == box3x and box4y == box3y):
    print("Box 4 placement failed, retrying...")
  else:
    break

while True:
  box5gridx = random.randint(0,9)
  box5gridy = random.randint(0,9)
  box5x = xlist[box5gridx]
  box5y = ylist[box5gridy]
  print(box5x,box5y)
  if (box5x == box1x and box5y == box1y) or (box5x == box2x and box5y == box2y) or (box5x == box3x and box5y == box3y) or (box5x == box4x and box5y == box4y):
    print("Box 5 placement failed, retrying...")
  else:
    break

while True:
  box6gridx = random.randint(0,9)
  box6gridy = random.randint(0,9)
  box6x = xlist[box6gridx]
  box6y = ylist[box6gridy]
  print(box6x,box6y)
  if (box6x == box1x and box6y == box1y) or (box6x == box2x and box6y == box2y) or (box6x == box3x and box6y == box3y) or (box6x == box4x and box6y == box4y) or (box6x == box5x and box6y == box5y):
    print("Box 6 placement failed, retrying...")
  else:
    break

while True:
  box7gridx = random.randint(0,9)
  box7gridy = random.randint(0,9)
  box7x = xlist[box7gridx]
  box7y = ylist[box7gridy]
  print(box7x,box7y)
  if (box7x == box1x and box7y == box1y) or (box7x == box2x and box7y == box2y) or (box7x == box3x and box7y == box3y) or (box7x == box4x and box7y == box4y) or (box7x == box5x and box7y == box5y) or (box7x == box6x and box7y == box6y):
    print("Box 7 placement failed, retrying...")
  else:
    break

hello.speed(speed)
hello.up()
hellolist1 = ["W","E","L","C","O","M","E"," !"]
for o in range(8):
  if o == 0:
    hello.goto(xlist[o+1]-5,xlist[8])
  elif o == 1:
    hello.goto(xlist[o+1]+2,xlist[8])
  elif o == 2:
    hello.goto(xlist[o+1]+4,xlist[8])
  elif o == 5:
    hello.goto(xlist[o+1]-3,xlist[8])
  else:
    hello.goto(xlist[o+1],xlist[8])
  hello.write(hellolist1[o], False, align="left", font=("Arial",40,))
hellolist4 = ["G","E","T"," ","A","L","L"," ","O","F"]
for o in range(10):
  hello.goto(xlist[o],xlist[6])
  hello.write(hellolist4[o], False, align="left", font=("Arial",40))
hellolist5 = ["T","H","E"," ","B","O","X","E","S"]

for o in range(9):
  hello.goto(xlist[o],xlist[5])
  hello.write(hellolist5[o], False, align="left", font=("Arial",40))
hellolist6 = ["T","O"," ","W","I","N"," !"]

for o in range(7):
  if o == 3:
    hello.goto(xlist[o+1]-5,xlist[4])
  elif o == 4:
    hello.goto(xlist[o+1]+10,xlist[4])
  else:
    hello.goto(xlist[o+1],xlist[4])
  hello.write(hellolist6[o], False, align="left", font=("Arial",40))
hellolist7 = ["W","A","S","D"," ","O","R"]
for o in range(7):
  if o == 0:
    hello.goto(xlist[o+1]-5,xlist[2])
  else:
    hello.goto(xlist[o+1],xlist[2])
  hello.write(hellolist7[o], False, align="left", font=("Arial",40))
hellolist8 = ["A","R","R","O","W"," ","K","E","Y","S"]
for o in range(10):
  if o == 4:
    hello.goto(xlist[o]-5,xlist[1])
  else:
    hello.goto(xlist[o],xlist[1])
  hello.write(hellolist8[o], False, align="Left", font=("Arial",40))
hellolist9 = ["T","O"," ","M","O","V","E","  ."]
for o in range(8):
  if o == 7:
    hello.goto(xlist[o],xlist[0])
  else:
    hello.goto(xlist[o+1],xlist[0])
  hello.write(hellolist9[o], False, align="Left", font=("Arial",40))

for o in range(5):
  hello.goto(xlist[o+2],xlist[9])
  hello.write(5-o, False, align="Left", font=("Arial",40,))
  #time.sleep(1)
hello.reset()
hello.ht()

def drawGhost(box, positionx, positiony):
  print("draw ghost:")
  print(positionx, positiony)
  box.ht()
  box.goto(positionx+22, positiony-22)
  box.clear()
  box.st()
  box.shape(image)
  
def ateGhost(box):
  box.clear()
  box.hideturtle()

box1=turtle.Turtle()
box2=turtle.Turtle()
box3=turtle.Turtle()
box4=turtle.Turtle()
box5=turtle.Turtle()
box6=turtle.Turtle()
box7=turtle.Turtle()
box1.ht()
box2.ht()
box3.ht()
box4.ht()
box5.ht()
box6.ht()
box7.ht()


#Making the first box
box1.speed(speed)

# box1.color("#ff4513")
# box1.up()
# box1.goto(box1x,box1y)
# box1.down()
# box1.begin_fill()
# for z in range(4):
#    box1.forward(40)
#    box1.right(90)
# box1.end_fill()

# box1xx = box1x + 22
# box1yy = box1y - 22

# print ("box1: ")
# print(box1x,box1y)
# print(box1xx,box1yy)
# box1.goto(box1xx,box1yy)
# box1.shape(image)
#box1.goto(225, 225)
drawGhost(box1, box1x, box1y)

# box2.speed(speed)
# box2.color("#004513")
# box2.up()
# box2.goto(box2x,box2y)
# box2.down()
# box2.begin_fill()
# for z in range(4):
#   box2.fd(40)
#   box2.rt(90)
# box2.end_fill()

# box3.speed(speed)
# box3.color("#004513")
# box3.up()
# box3.goto(box3x,box3y)
# box3.down()
# box3.begin_fill()
# for z in range(4):
#   box3.fd(40)
#   box3.rt(90)
# box3.end_fill()

# box4.speed(speed)
# box4.color("#004513")
# box4.up()
# box4.goto(box4x,box4y)
# box4.down()
# box4.begin_fill()
# for z in range(4):
#   box4.fd(40)
#   box4.rt(90)
# box4.end_fill()

# box5.speed(speed)
# box5.color("#004513")
# box5.up()
# box5.goto(box5x,box5y)
# box5.down()
# box5.begin_fill()
# for z in range(4):
#   box5.fd(40)
#   box5.rt(90)
# box5.end_fill()

# box6.speed(speed)
# box6.color("#004513")
# box6.up()
# box6.goto(box6x,box6y)
# box6.down()
# box6.begin_fill()
# for z in range(4):
#   box6.fd(40)
#   box6.rt(90)
# box6.end_fill()

drawGhost(box1, box1x, box1y)
drawGhost(box2, box2x, box2y)
drawGhost(box3, box3x, box3y)
drawGhost(box4, box4x, box4y)
drawGhost(box5, box5x, box5y)
drawGhost(box6, box6x, box6y)

box7.speed(speed)
# box7.color("#004513")
# box7.up()
# box7.goto(box7x,box7y)
# box7.down()
# box7.begin_fill()
# for z in range(4):
#   box7.fd(40)
#   box7.rt(90)
# box7.end_fill()
drawGhost(box7, box7x, box7y)

playerx = playery = 4
boxes = 7
haswon = 0
player=turtle.Turtle()
player.ht()

def boxcheck():
  global box1gridx; global box1gridy; global box2gridx; global box2gridy; global box3gridx; global box3gridy; global box4gridx; global box4gridy; global box5gridx; global box5gridy; global box6gridx; global box6gridy; global box7gridx; global box7gridy; global boxes
  if playerx == box1gridx and playery == box1gridy:
    ateGhost(box1)
    boxes -= 1
    box1gridx = box1gridy = -1
  elif playerx == box2gridx and playery == box2gridy:
    ateGhost(box2)
    boxes -= 1
    box2gridx = box2gridy = -1
  elif playerx == box3gridx and playery == box3gridy:
    ateGhost(box3)
    boxes -= 1
    box3gridx = box3gridy = -1
  elif playerx == box4gridx and playery == box4gridy:
    ateGhost(box4)
    boxes -= 1
    box4gridx = box4gridy = -1
  elif playerx == box5gridx and playery == box5gridy:
    ateGhost(box5)
    boxes -= 1
    box5gridx = box5gridy = -1
  elif playerx == box6gridx and playery == box6gridy:
    ateGhost(box6)
    boxes -= 1
    box6gridx = box6gridy = -1
  elif playerx == box7gridx and playery == box7gridy:
    ateGhost(box7)
    boxes -= 1
    box7gridx = box7gridy = -1
  if boxes == 0:
    win()

def win():
  global haswon; global playerx; global playery
  print("You win!! :)")
  if haswon == 0:
    haswon = 1
    winner.speed(speed)
    winner.up()
    winlist = ["Y","O","U"," ","W","O","N"," !"]
    for o in range(8):
      if o == 0:
        winner.goto(xlist[o+1]+2,xlist[5])
      elif o == 4:
        winner.goto(xlist[o+1]-5,xlist[5])
      else:
        winner.goto(xlist[o+1],xlist[5])
      winner.write(winlist[o], False, align="left", font=("Arial",40,))
    playerx = playery = 10
    drawplayer()

def drawplayer():
  boxcheck()
  player.clear()
  player.speed(speed)
  player.up()
  player.goto(playerposlist[playerx],playerposlist[playery])
  #player.dot(20,"#ABCDEF")
  player.showturtle()
  player.shape(pacimage)

drawplayer()

def up():
  global playery
  if playery < 9:
    playery += 1
    drawplayer()

def down():
  global playery
  if playery > 0 and playery < 10:
    playery -= 1
    drawplayer()

def left():
  global playerx
  if playerx > 0 and playerx < 10:
    playerx -= 1
    drawplayer()

def right():
  global playerx
  if playerx < 9:
    playerx += 1
    drawplayer()

window.onkey(up, "Up")
window.onkey(up, "W")
window.onkey(down, "Down")
window.onkey(down, "S")
window.onkey(left, "Left")
window.onkey(left, "A")
window.onkey(right, "Right")
window.onkey(right, "D")

window.listen()
window.mainloop()