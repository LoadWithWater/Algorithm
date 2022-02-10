n, k = map(int,input().split())
people = [i for i in range(1, n+1)] # 처음 지정된 사람들의 배열

result = [] # 출력
num = 0 # 인덱스

for i in range(n):
    num += k-1  # K-1을 해주는 이유는 배열인덱스는 0부터 시작하기 때문
    if num >= len(people):
        num = num % len(people)
 
    result.append(str(people.pop(num)))
print("<", ", ".join(result)[:], ">", sep='')