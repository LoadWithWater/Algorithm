from collections import deque   # 큐를 사용하기에 deque를 불러와줍니다.
import sys      # sys 모듈을 불러옵니다.

T = int(input())    # 테스트 케이스를 받습니다.


for i in range(T):
    N, M = map(int,input().split())
    printer = deque(list(map(int, sys.stdin.readline().split())))
    count = 0

    
