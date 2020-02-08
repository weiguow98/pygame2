import turtle
import keyboard 

screen = turtle.Screen()

# click the image icon in the top right of the code window to see
# which images are available in this trinket
image = "C:/Users/wan020336/Documents/Python/pygame/ghost.gif"

# add the shape first then set the turtle shape
screen.addshape(image)
turtle.speed(10)
turtle.penup()
turtle.shape(image)
turtle.goto(300,100)
#turtle..forward(300)

screen.bgcolor("lightblue")

move_speed = 10
turn_speed = 10

# these defs control the movement of our "turtle"
def forward():
  turtle.forward(move_speed)

def backward():
  turtle.backward(move_speed)

def left():
  turtle.left(turn_speed)

def right():
  turtle.right(turn_speed)

turtle.penup()
turtle.speed(0)
# turtle.home()

# now associate the defs from above with certain keyboard events
screen.onkey(forward, "Up")
screen.onkey(backward, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.listen()

a = keyboard.read_key()
