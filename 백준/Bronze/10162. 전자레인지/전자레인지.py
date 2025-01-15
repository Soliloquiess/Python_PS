T = int(input())

if T % 10 != 0:
    print(-1)
else:
    A = T // 300  # A 버튼 (5분)
    T %= 300
    B = T // 60   # B 버튼 (1분)
    T %= 60
    C = T // 10   # C 버튼 (10초)
    
    print(A, B, C)
