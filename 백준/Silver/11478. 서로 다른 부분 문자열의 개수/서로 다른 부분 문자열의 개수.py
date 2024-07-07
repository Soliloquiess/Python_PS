s = input()

# 서로 다른 부분 문자열을 저장할 집합
unique_substrings = set()

# 문자열의 길이
length = len(s)

# 모든 부분 문자열 생성
for i in range(length):
    for j in range(i + 1, length + 1):
        # 부분 문자열을 집합에 추가
        unique_substrings.add(s[i:j])

# 집합의 크기를 출력 (서로 다른 부분 문자열의 개수)
print(len(unique_substrings))
