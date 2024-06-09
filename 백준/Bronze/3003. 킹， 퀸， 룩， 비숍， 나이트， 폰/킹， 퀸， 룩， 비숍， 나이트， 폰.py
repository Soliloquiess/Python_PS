# 올바른 피스의 개수
correct_pieces = [1, 1, 2, 2, 2, 8]

# 입력 받기
found_pieces = list(map(int, input().split()))

# 각 피스의 차이를 계산하여 출력
result = [correct_pieces[i] - found_pieces[i] for i in range(6)]

# 결과 출력
print(' '.join(map(str, result)))
