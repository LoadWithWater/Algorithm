import math

N = int(input()) #사람 수 입력 받기

Gamers = list(range(1, N+1))

i = 0
GameCount = N-1
while True:
  if i == GameCount:
    break
  else:
    i += 1

  mul = int(math.pow(i, 3))
  Del = mul % len(Gamers)
  if Del != 0:
    Del -= 1
  Gamers.pop(Del)

print(Gamers[0])