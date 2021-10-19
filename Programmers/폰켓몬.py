# 폰켓몬
def solution(nums):
    answer = 0
    # nums의 길이 반이 고를 수 있는 폰켓몬의 수
    pick = len(nums) / 2
    # nums를 집합 자료형 변환하여 중복 제거후 다시 리스트 변환
    nums = list(set(nums))
    # 중복을 제거한 nums의 길이가 pick과 크거나 같으면 가질 수 있는 최대 종류는 pick과 같다.
    if len(nums) >= pick:
        answer = pick
    # nums의 길이가 작은 경우 그 만큼의 종류를 가질 수 있다.
    elif len(nums) < pick:
        answer = len(nums)
    return answer
print(solution([3, 1, 2, 3]))

# def solution(nums):
#     answer = 0
#     length = len(nums) // 2
#     temp = list(set(nums))
#
#     for value in temp:
#         if (answer < length):
#             answer += 1
#
#     return answer