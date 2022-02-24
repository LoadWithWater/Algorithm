import sys      # sys 모듈을 불러옵니다.
N = int(input())   # 명령 개수를 입력합니다.

stack = [] # 스택을 저장할 리스트입니다.

for i in range(N):  # 입력한 명령 수 만큼 반복합니다.
    com = sys.stdin.readline().split()  # 명령을 입력하는 곳입니다. input말고 sys.stdin.readline.split()을 이용하여
                                        # "push 1" 같은 명령을 받을 수 있고 split을 사용하여 분리가 가능합니다.
                                        # 또한 input을 사용하여 나오는 시간초과를 방지할 수 있습니다.

    if com[0] == 'push':    # push 명령
        stack.append(com[1])

    elif com[0] == 'pop':   # pop 명령
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())

    elif com[0] == 'size':  # size 명령
        print(len(stack))

    elif com[0] == 'empty': # empty 명령
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    
    elif com[0] == 'top':   # top 명령
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])