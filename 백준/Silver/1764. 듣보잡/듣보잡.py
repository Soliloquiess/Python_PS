# 첫 번째 줄에서 듣도 못한 사람의 수 N과 보도 못한 사람의 수 M을 입력 받습니다.
first_line = input().strip().split()
N = int(first_line[0])
M = int(first_line[1])

# 듣도 못한 사람의 이름들을 저장할 집합
not_heard = set()
for _ in range(N):
    not_heard.add(input().strip())

# 보도 못한 사람의 이름들을 저장할 집합
not_seen = set()
for _ in range(M):
    not_seen.add(input().strip())

# 듣도 보도 못한 사람 = 듣도 못한 사람 집합과 보도 못한 사람 집합의 교집합을 구합니다.
intersection = sorted(not_heard & not_seen)

# 결과 출력
print(len(intersection))
for person in intersection:
    print(person)

