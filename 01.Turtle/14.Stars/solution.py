import turtle as t

def drawStar(rays):
  angle = 180 - 180/rays
  for x in range(rays):
    t.forward(100)
    t.left(angle)

def relocate(coordinates):
  t.penup()
  t.goto(coordinates)
  t.pendown()

for x in 5, 11:
  relocate((x*40 - 300, 0))
  drawStar(x)

t.done()
