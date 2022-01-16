def solution(brown, yellow):
    answer = []
    total = brown + yellow  # a * b = total
    for b in range(1, total + 1):
        if (total / b) % 1 == 0:  # total / b = a
            a = total / b
            if a >= b:  # a >= b
                if 2 * a + 2 * b == brown + 4:  # 2*a + 2*b = brown + 4
                    return [a, b]

    return answer

# def solution(brown, yellow):
#     s = brown + yellow
#     for i in range(s,2,-1): # 가로
#         if s % i == 0:
#             a= s // i
#             if yellow == (i-2)*(a-2):
#                 return [i, a]
#https://it-garden.tistory.com/361

print(solution(10,2));
print(solution(8,1));
print(solution(24,24));