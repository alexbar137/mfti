import turtle as t

def drawFace():
  t.fillcolor("yellow")
  t.begin_fill()
  t.circle(50, steps=100)
  t.end_fill()

def relocate(coordinates):
  t.penup()
  t.goto(coordinates)
  t.pendown()

def drawEye():
  t.fillcolor("blue")
  t.begin_fill()
  t.circle(10, steps=50)
  t.end_fill()

def drawNose():
  t.setheading(270)
  t.pensize(10)
  t.forward(20)

def drawMouth():
  t.setheading(270)
  t.color("red")
  t.circle(-30, 180, 50)

drawFace()
relocate((-20, 65))
drawEye()
relocate((20, 65))
drawEye()
relocate((0, 60))
drawNose()
relocate((30, 40))
drawMouth()
t.done()