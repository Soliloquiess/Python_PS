def solution(my_string, m, c):
    answer = ''
    rows = len(my_string) // m  # 줄 수 계산

    for i in range(rows):
        answer += my_string[i * m + (c - 1)]

    return answer
