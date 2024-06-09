words = input().upper()
unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거

# 각 알파벳의 빈도를 계산하여 딕셔너리로 저장
frequency = {}
for char in unique_words:
    frequency[char] = words.count(char)

max_count = max(frequency.values())

# 빈도가 최대값인 알파벳들을 찾기
max_chars = []
for char, count in frequency.items():
    if count == max_count:
        max_chars.append(char)

if len(max_chars) > 1:  # 빈도가 최대값인 알파벳이 여러 개라면
    print('?')
else:
    print(max_chars[0])


# words = input().upper()
# unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거
#
# # 각 알파벳의 빈도를 계산하여 딕셔너리로 저장
# frequency = {}
# for char in unique_words:
#     count = 0
#     for c in words:
#         if char == c:
#             count += 1
#     frequency[char] = count
#
# # 최대값을 찾기 위한 초기화
# max_count = 0
# max_chars = []
#
# # 최대값을 찾으면서 최대값인 알파벳들을 찾기
# for char, count in frequency.items():
#     if count > max_count:
#         max_count = count
#         max_chars = [char]
#     elif count == max_count:
#         max_chars.append(char)
#
# if len(max_chars) > 1:  # 빈도가 최대값인 알파벳이 여러 개라면
#     print('?')
# else:
#     print(max_chars[0])
