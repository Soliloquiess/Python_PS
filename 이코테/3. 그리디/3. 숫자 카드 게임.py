# 반복문 사용한 예.
# N, M을 공백을 기준으로 구분하여 입력 받기
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    # 현재 줄에서 '가장 작은 수' 찾기
    min_value=10001;
    for a in data:
        min_value = min(a,min_value)

    result = max(result, min_value)

print(result) # 최종 답안 출력
#뭔가 무수한 에러가 났는데 탭 키 대신 스페이스바 4번 누르니까 정렬이라던가
#IndentationError: unindent does not match any outer indentation level 의 문제가 해결되었다.





# min 함수 이용하는 예
# n, m = map(int, input().split())
# result = 0
# 한 줄씩 입력 받아 확인하기
# for i in range(n):
#     data = list(map(int, input().split()))
#     # 현재 줄에서 '가장 작은 수' 찾기
#     min_value = min(data)
#     # '가장 작은 수'들 중에서 가장 큰 수 찾기
#     result = max(result, min_value)
#
# print(result) # 최종 답안 출력


# 3 3
# 3 1 2
# 4 1 4
# 2 2 2


# 2 4
# 7 3 1 8
# 3 3 3 4