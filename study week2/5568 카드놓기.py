import itertools # 순열 구할때 쓰기

n = int(input())
k = int(input())
cards = []

for i in range(n):
    a = int(input())
    cards.append(a)

print(cards)
nCr_cards = itertools.permutations(cards, n)
print(nCr_cards)