from collections import deque   # 큐를 사용하기에 deque를 불러와줍니다.

N = int(input())    # N장의 카드를 입력받습니다.
cards = deque([i for i in range(1, N+1)])   # 카드는 1부터 시작하기에 range(1, N+1)을 써서 1부터 시작하는 큐로 만듭니다.


while(len(cards) > 1):  # 1장이 남을 때 까지 반복합니다.
    cards.popleft()     # collections 모듈을 불러왔기 때문에 popleft를 사용할 수 있습니다. 맨 앞에 있는 값을 쉽게 제거 할 수 있습니다.
    temp = cards.popleft()  # 카드뭉치에서 맨 앞에 값을 popleft를 써서 제거하고 이를 임시 변수 temp에 넣습니다.
    cards.append(temp)      # temp를 카드 맨 뒤에 넣습니다.
    
print(cards[0]) # 카드 출력


# 리스트로 풀면 시간 초과가 뜹니다!
# N = int(input())

# cards = list(range(1, N+1))

# while (len(cards) > 1):
#     cards.pop(0)
#     temp = cards.pop(0)
#     cards.append(temp)

# print(cards[0])
