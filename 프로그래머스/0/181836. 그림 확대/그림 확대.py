def solution(picture, k):
    answer = []
    for row in picture:
        # 1. 각 문자를 가로로 k배
        #new_row = ''.join([c * k for c in row])
        new_row = ""
        for c in row:
            new_row += c * k
        # 2. 그 줄을 세로로 k배
        for _ in range(k):
            answer.append(new_row)
    return answer
