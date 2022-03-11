from collections import deque
N = int(input())
Balloons = deque(list(map(int, input().split())))
result = []

while Balloons:
    Balloon, paper = Balloons.popleft()
    result.append(Balloon + 1)
    if paper > 0:
        Balloons.rotate(-(paper-1))
    elif paper < 0:
        Balloons.rotate(-paper)

print(' '.join(map(str, result)))