# 풀이 1
def solution(x, n):
    result = [x]
    for i in range(2, n+1):
        result.append(x * i)
    return result

# # 풀이 2 - list comprehension 활용
# def solution(x, n):
#     return [x*i for i in range(1, n+1)]
#
#
# # 풀이 3 - list() 함수 활용
# def solution(x, n):
#     return list(range(x, x*n+1, x))
print(solution(2,5))
