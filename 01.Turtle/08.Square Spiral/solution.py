import turtle as t

k = 1.5
BASE_DISTANCE = 5

for x in range(100):
  t.forward(x * k * BASE_DISTANCE)
  t.right(90)

t.done()