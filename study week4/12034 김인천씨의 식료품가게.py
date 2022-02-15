T = int(input())  # 테스트 케이스 입력

for i in range(T):
    N = int(input()) # 상품 개수 입력
    all = list(map(int, input().split())) # 뒤죽박죽 된 상품 가격들입니다.
    discount = [] # 할인 된 가격의 상품들을 모아놓는 배열입니다.

    while (len(discount) != N): # 할인 된 상품 갯수(discount 배열 길이)가 상품 개수(N)와 같아질 때까지 무한반복합니다.

        product = all[-1] # product라는 변수에 all의 마지막 값을 넣습니다.
        dis_product = int(int(product)*0.75) # dis_product = product의 할인 가격

        discount.append(dis_product) # discount에 할인된 가격을 추가합니다.
        all.remove(dis_product) # all에서는 할인된 가격을 뺍니다.
        all.pop() # 마지막 값도 빼줍니다.

    discount.reverse() # 최대값부터 찾아나갔으므로 discount는 값이 내림차순으로 쌓입니다. 오름차순으로 출력하기위해 reverse를 적용합니다.
    lst_discount = [str(a) for a in discount]
    print("Case #" + str(i+1) + ": " +" ".join(lst_discount))