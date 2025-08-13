def solution(binomial):
    a, op, b = binomial.split()   # 공백 기준으로 3부분 분리
    a = int(a)
    b = int(b)
    
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    else:  # op == '*'
        return a * b
