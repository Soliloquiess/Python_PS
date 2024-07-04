n = int(input())  # 로그의 개수 입력 받기
logs = []  # 로그를 저장할 리스트

# n개의 로그를 입력받아 리스트에 추가
for _ in range(n):
    log = input().strip()  # 로그를 입력받고 공백을 제거
    logs.append(log)  # 로그를 리스트에 추가
#logs = [input().strip() for _ in range(n)]

# 현재 회사에 있는 사람을 저장할 집합
current_people = set()

# 출입 기록 처리
for log in logs:
    name, action = log.split()
    if action == "enter":
        current_people.add(name)
    elif action == "leave":
        current_people.remove(name)

# 현재 회사에 있는 사람들 이름을 사전 역순으로 정렬
result = sorted(current_people, reverse=True)

for person in result:
    print(person)
