N, M = map(int,input().split()) # 교과서 수 N, 교과서 더미 수 M
result = True

for i in range(M):
    j = int(input()) # 더미의 책 개수
    dummy = list(map(int, input().split()))

    for k in range(i-1):
        if k[i] < k[i+1]:
            result = False
            break

if (result == True):
    print("Yes")
else:
    print("No")