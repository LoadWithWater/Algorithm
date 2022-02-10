n, m = map(int,input().split())
count = 0 # 최종 CD 개수

for i in range(n):
    sang = []
    s = int(input())
    sang.append(s)

for j in range(m):
    sun = []
    su = int(input())
    sun.append(su)

print("0 0")

for j in range(len(sang)):
    for k in range(len(sun)):
        if (sang[j] == sun[k]):
            count += 1

print(count)