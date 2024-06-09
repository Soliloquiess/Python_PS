# 입력 받기
A, B = input().split()

# 숫자를 거꾸로 읽기
reversed_A = int(A[::-1])
reversed_B = int(B[::-1])

# 큰 숫자 찾기
if reversed_A > reversed_B:
    print(reversed_A)
else:
    print(reversed_B)


# A, B = map(str, input().split())
# A = int(A[2]+A[1]+A[0])
# B = int(B[2]+B[1]+B[0])
# print(max(A, B))