# 입력
S = input().strip()

# 알파벳 위치를 저장할 리스트 (-1로 초기화)
positions = [-1] * 26

# 문자열 S를 순회하면서 위치를 기록
for index, char in enumerate(S):
    pos = ord(char) - ord('a')
    if positions[pos] == -1:  # 처음 등장하는 위치만 저장
        positions[pos] = index

# 결과 출력
print(' '.join(map(str, positions)))

# S = input()
# check = [-1] * 26
#
# for i in range(len(S)):
#     if check[ord(S[i]) - 97] != -1:
#         continue
#     else:
#         check[ord(S[i]) - 97] = i
#
# for i in range(26):
#     print(check[i], end=' ')