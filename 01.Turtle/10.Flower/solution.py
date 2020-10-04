import turtle as t

def drawCircle():
  for x in range(36):
    t.forward(10)
    t.left(10)

for x in range(6):
  drawCircle()
  t.left(60)

t.done()