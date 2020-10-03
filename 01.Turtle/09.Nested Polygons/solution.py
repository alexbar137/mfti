import turtle as t

BASE_SIZE = 10

def makePolygon(corners, size):
  internalAngle = (corners - 2) / corners * 180
  externalAngle = 180 - internalAngle
  t.left(180 - internalAngle/2)
  for x in range(corners):
    t.forward(size)
    t.left(externalAngle)

def relocate():
  t.penup()
  t.setheading(0)
  t.forward(BASE_SIZE*1.5)
  t.pendown()

for x in range(3, 14):
  size = BASE_SIZE*x
  relocate()
  makePolygon(x, size)

t.done()