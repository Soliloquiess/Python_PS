n, m = map(int, input().split())    #5 21을 넣어서 (카드 개수, 목표 숫자)
a = list(map(int, input().split())) # 카드 적힌 번호들 넣어줌
b = len(a)
sum = 0
for i in range(0, b - 2):   #3개 고르기 떄문에 첫 카드는 N-2까지만 순회
        for j in range(i + 1, b - 1):   #두번째 카드는 첫 카드 다음부터 n-1까지만 순회
                for k in range(j + 1, b):   #세번째 카드는 두번쨰 카드 다음부터 N까지 순회
                        if a[i] + a[j] + a[k] > m:  #3카드 합이 m보다 크면 무시
                                continue
                        else:   #m보다 크지 않으면 일단은 정답 가능성 존재
                                sum = max(sum, a[i] + a[j] + a[k])
print(sum)

# https://duwjdtn11.tistory.com/297