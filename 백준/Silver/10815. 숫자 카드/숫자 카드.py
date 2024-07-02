# 입력 받기
import sys
input = sys.stdin.read
data = input().split()

n = int(data[0])
cards = set(map(int, data[1:n+1]))
m = int(data[n+1])
queries = list(map(int, data[n+2:]))

# 결과를 저장할 리스트
results = []

# 집합을 사용하여 존재 여부 확인
for query in queries:
    if query in cards:
        results.append(1)
    else:
        results.append(0)

# 결과 출력
print(" ".join(map(str, results)))
