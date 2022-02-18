# 답을 맞혔지만 시간이 너무 오래 걸립니다!!!!!
# 추후 다른 방법으로 풀기바람

N, M = map(int,input().split()) # 케이스 입력

people = {} # 모든 사람들의 정보를 담는 딕셔너리입니다.

for _ in range(N):  # 우선 듣지 못한 사람들을 넣습니다. 여기서는 그냥 넣어도 됩니다.
    listen = input()
    people[listen] = 1

for _ in range(M):  # 보지 못한 사람들을 넣습니다. 여기서는 듣지 못한 사람들과 중복될 수 있기 때문에 if문을 써서 중복 처리를 합니다.
    watch = input()
    if (watch not in people):
        people[watch] = 1
    else:
        people[watch] += 1

people_keys = list(people.keys()) # 사람 이름을 리스트로 표현합니다.
people_values = list(people.values()) # 사람 수를 리스트로 표현합니다.
listenandwatch = [] # 듣도 보도 못한 사람들의 이름을 넣는 곳입니다.

for i in range(len(people_values)):     # 만약 사람 수가 2라면(듣도 보도 못한 사람) listenandwatch에 사람 이름을 넣습니다.
    if (people_values[i] == 2):
        listenandwatch.append(people_keys[i])

result = sorted(listenandwatch) # 문제에서 사전 순으로 정렬하라고 하였기에 sorted를 사용합니다.
print(len(result))  # 사람 수 출력
for j in range(len(result)):    # 사람 이름 출력
    print(result[j])