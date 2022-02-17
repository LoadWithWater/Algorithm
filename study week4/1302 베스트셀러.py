N = int(input())  # 책 수 입력 받기

books = {} # 입력받는 모든 책 정보입니다.
           # 딕셔너리로 구성하였으며 key는 책이름 value는 권 수 입니다.
for _ in range(N):
    book = input()
    if (book not in books):
        books[book] = 1
    else:
        books[book] += 1

bestcellers = dict(sorted(books.items(), key=lambda x: x[1], reverse=True))  # 출처 : https://blockdmask.tistory.com/566
    # 이 코드는 dictionary의 value값을 기준으로 내림차순 정렬하는 코드입니다. 출처는 위에 있습니다.

bestceller_keys = list(bestcellers.keys())   # list(딕셔너리.keys()) : key로 리스트를 만듭니다.
bestceller_values = list(bestcellers.values())   # list(딕셔너리.values()) : values로 리스트를 만듭니다.
result = []   # 출력할 책 제목을 모아놓는 곳입니다. 
              # 리스트로 쓰는 이유는 중복된 값이 있을 수 있으므로 값들을 일단 받아놓고 나중에 출력할 때 sorted를 쓰면 됩니다.
              # 문제에서 사전순으로 출력하라고 했으므로 sorted 사용예정

for i in range(len(bestceller_keys)):
    if(bestceller_values[i] == bestceller_values[0]):
        result.append(bestceller_keys[i])

print(sorted(result)[0])