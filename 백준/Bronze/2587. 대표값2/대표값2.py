# 다섯 개의 자연수를 입력받습니다.
numbers = []
for _ in range(5):
    numbers.append(int(input().strip()))

# 평균을 계산합니다.
average = sum(numbers) // len(numbers)

# 중앙값을 계산합니다.
numbers.sort()
median = numbers[2]

# 결과를 출력합니다.
print(average)
print(median)
