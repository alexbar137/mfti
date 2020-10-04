import turtle as t
import math

BASE_DIAMETER = 20
INCREASE = 2

def drawCircle(diameter):
  c = math.pi * abs(diameter)
  direction = diameter/abs(diameter)
  for x in range(36):
    t.forward(c/10)
    t.left(direction * 10)

t.setheading(90)
for x in range(10):
  diameter = BASE_DIAMETER + x*INCREASE
  drawCircle(diameter)
  drawCircle(-diameter)

t.done()
