# 입력 받기
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
cards = list(map(int, data[1:n+1]))
m = int(data[n+1])
queries = list(map(int, data[n+2:]))

# 상근이가 가진 숫자 카드를 정렬
cards.sort()

# 결과를 저장할 리스트
results = []

# 이진 탐색 직접 구현
for query in queries:
    left, right = 0, len(cards) - 1
    found = 0
    while left <= right:
        mid = (left + right) // 2
        if cards[mid] == query:
            found = 1
            break
        elif cards[mid] < query:
            left = mid + 1
        else:
            right = mid - 1
    results.append(found)

print(" ".join(map(str, results)))
