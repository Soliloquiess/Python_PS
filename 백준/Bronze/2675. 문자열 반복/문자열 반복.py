# 입력 받기
T = int(input().strip())  # 테스트 케이스의 개수

results = []

# 각 테스트 케이스 처리
for _ in range(T):
    R, S = input().strip().split()
    R = int(R)

    # 새로운 문자열 P 생성
    P = ''
    for char in S:
        P += char * R

    # 결과 저장
    results.append(P)

# 결과 출력
for result in results:
    print(result)


# n = int(input())
# for i in range(n):
#     num, str = input().split()
#     text = ''
#     for i in str:
#         text += int(num) * i
#     print(text)