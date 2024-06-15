# 다섯 줄의 입력을 리스트로 저장합니다.
words = [input().strip() for _ in range(5)]

# 결과를 저장할 문자열 초기화
result = ""

# 가장 긴 문자열의 길이를 찾습니다.
max_length = max(len(word) for word in words)

# 각 열(column)을 순회합니다.
for i in range(max_length):
    # 각 행(row)에서 해당 인덱스의 문자를 결과에 추가합니다.
    for word in words:
        if i < len(word):
            result += word[i]

# 결과 출력
print(result)
