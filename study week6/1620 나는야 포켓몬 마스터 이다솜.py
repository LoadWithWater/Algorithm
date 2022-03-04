# 시간 초과

N, M = map(int, input().split())

pokemon_dic = {}
poke_num = 0

for i in range(N):
    pokemon = input()
    pokemon_dic[pokemon] = poke_num
    poke_num += 1

pokemon_keys = list(pokemon_dic.keys())

for j in range(M):
    quiz = input()

    if quiz.isdigit():
        print(pokemon_keys[int(quiz)-1])
    else:
        print((pokemon_dic[quiz])+1)