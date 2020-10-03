import turtle as t

def makeSpider(legs):
  t.shape("turtle")
  ANGLE = 360/legs
  for x in range(legs):
    makeLeg(ANGLE)

def makeLeg(angle):
  t.forward(100)
  t.stamp()
  t.goto((0,0))
  t.right(angle)

for x in range(2, 13):
  t.clearscreen()
  makeSpider(x)

input()