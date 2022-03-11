# 후위 표기법으로 표현된 수식을 계산하는 프로그램 구현
# 1. 피연산자는 무조건 스택으로 옮긴다.
# 2. 연산자를 만나면 스택에서 두 개의 피연산자를 꺼내서 계산을 한다.
# 3. 계산결과는 다시 스택에 넣는다.
# 출처 : 윤성우의 열혈 자료구조 p240



N = int(input())    # 피연산자 개수를 입력받습니다.
Postfix = input()   # 후위 표기식을 입력받습니다.
num = []            # 피연산자(숫자)를 저장할 리스트입니다.
stack = []          # 계산할 스택입니다.

for i in range(N):
    num.append(int(input()))    # for문을 이용하여 num에 피연산자(숫자)를 입력받습니다.

Postfix_array = list(Postfix)
print(Postfix_array)


count = 0           # num에서 Postfix_array에 값을 집어넣는 역할을 하는 count입니다
for j in range(len(Postfix_array)):
    if ('A' <= Postfix_array[j] <= 'Z'):
        Postfix_array[j] = num[count]
        count += 1


for k in range(len(Postfix_array)):
    if (type(Postfix_array[k]) == int):
        stack.append(Postfix_array[k])
    else:
        second = stack.pop()
        first = stack.pop()

        if (Postfix_array[k] == '+'):
            stack.append(first + second)
        elif (Postfix_array[k] == '-'):
            stack.append(first - second)
        elif (Postfix_array[k] == '*'):
            stack.append(first * second)
        elif (Postfix_array[k] == '/'):
            stack.append(first / second)

print('%.2f' %stack[0])