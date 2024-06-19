# 세 막대의 길이를 입력받습니다.
a, b, c = map(int, input().split())

# 세 변의 길이를 내림차순으로 정렬합니다.
sticks = [a, b, c]
sticks.sort(reverse=True)

# 가장 긴 막대의 길이를 다른 두 막대의 합보다 작도록 줄입니다.
while sticks[0] >= sticks[1] + sticks[2]:
    sticks[0] -= 1

# 가장 큰 삼각형의 둘레를 계산합니다.
perimeter = sum(sticks)

# 결과를 출력합니다.
print(perimeter)
