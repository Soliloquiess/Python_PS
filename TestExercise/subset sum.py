def deQuote(list):
    for i in range(0, len(list)):
        list[i] = int(list[i])

def findMaxSpan(list, k):
    size = len(list)                                        # 목록의 길이
    max = list[0]                                           # 임시 최대 구간합

    for start in range(0, size - k + 1):                    # strat = 구간 출발 위치
        sum = list[start]                                   # 현재 구간 합 초기화

        for i in range(1, k):                               # 현재 구간 내 원소들
            sum += list[start +i]                           # 원소 합산

        if sum > max:                                       # 최대 구간합 갱신
            max = sum

    return max

list = input("정수들의 목록을 입력하세요 : ").split()
deQuote(list)
k = int(input("최대 구간합을 구할 구간 수(k) : "))

max = findMaxSpan(list, k)

print("최대 {}-구간합 : {}".format(k, max))