def solution(ineq, eq, n, m):
    # 조건에 맞는 비교를 진행하여 answer에 결과를 저장
    if ineq == "<" and eq == "=":
        if n <= m:
            answer = 1
        else:
            answer = 0
    elif ineq == ">" and eq == "=":
        if n >= m:
            answer = 1
        else:
            answer = 0
    elif ineq == "<" and eq == "!":
        if n < m:
            answer = 1
        else:
            answer = 0
    elif ineq == ">" and eq == "!":
        if n > m:
            answer = 1
        else:
            answer = 0
    return answer
