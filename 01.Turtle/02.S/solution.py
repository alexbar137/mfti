import turtle as t

def forwardRight():
  for x in range(2):
    t.forward(50)
    t.left(90)

def forwardLeft():
  for x in range(2):
    t.forward(50)
    t.right(90)

forwardRight()
forwardLeft()
t.forward(50)

t.done()