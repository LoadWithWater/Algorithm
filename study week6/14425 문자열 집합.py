# 정답을 맞혔지만 시간이 너무 오래 걸립니다!!!

N, M = map(int, input().split()) # N개의 문자열 개수를 받고 M개의 체크할 문자열 개수를 받습니다.
S = []     # 집합 S입니다. (N개의 문자열이 들어갑니다.)
count = 0  # 카운트입니다.

for i in range(N):
    S.append(input())   # for문을 이용하여 집합 S에 들어갈 N개의 문자열을 받습니다.

for j in range(M):
    check = input()     # check 변수에 문자열을 입력받습니다.
    if check in S:      # 만약 check가 집합 S에 있는 문자열이라면 카운트 1을 더합니다. 이를 M번 반복합니다.
        count += 1

print(count)            # 카운트 출력