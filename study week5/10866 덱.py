from collections import deque   # 큐를 사용하기에 deque를 불러와줍니다.
import sys      # sys 모듈을 불러옵니다.

N = int(input())    # 명령 개수를 입력합니다.
Deq = deque([])     # 덱을 저장할 큐입니다.

for i in range(N):   # 입력한 명령 수 만큼 반복합니다.
    com = sys.stdin.readline().split()  # 명령을 입력하는 곳입니다. input말고 sys.stdin.readline.split()을 이용하여
                                        # "push_front 1" 같은 명령을 받을 수 있고 split을 사용하여 분리가 가능합니다.
                                        # 또한 input을 사용하여 나오는 시간초과를 방지할 수 있습니다.

    if com[0] == "push_front":  # push_front 명령
        Deq.appendleft(com[1])  # collection 모듈에 있는 deque는 양방향 큐입니다.
                                # appendleft를 사용하여 앞에도 값을 쉽게 추가할 수 있습니다.

    elif com[0] == "push_back": # push_back 명령
        Deq.append(com[1])

    elif com[0] == "pop_front": # pop_front 명령
        if len(Deq) == 0:
            print(-1)
        else:
            print(Deq.popleft())    # appendleft와 같이 popleft를 사용하여 맨앞에 있는 값을 쉽게 제거 할 수 있습니다.

    elif com[0] == "pop_back":      # pop_back 명령
        if len(Deq) == 0:
            print(-1)
        else:
            print(Deq.pop())

    elif com[0] == 'size':  # size 명령
        print(len(Deq))

    elif com[0] == 'empty': # empty 명령
        if not Deq:
            print(1)
        else:
            print(0)

    elif com[0] == 'front': # front 명령
        if not Deq:
            print(-1)
        else:
            print(Deq[0])

    elif com[0] == 'back':  # back 명령
        if not Deq:
            print(-1)
        else:
            print(Deq[-1])