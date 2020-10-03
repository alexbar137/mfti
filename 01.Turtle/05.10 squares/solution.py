import turtle as t

BASE_SIZE = 20

def square(size):
  for x in range(4):
    t.forward(size)
    t.right(90)

def relocate():
  DISTANCE = BASE_SIZE/2
  t.penup()
  t.back(DISTANCE)
  t.left(90)
  t.forward(DISTANCE)
  t.right(90)
  t.pendown()

for x in range(1, 11):
  square(x * BASE_SIZE)
  relocate()

t.done()