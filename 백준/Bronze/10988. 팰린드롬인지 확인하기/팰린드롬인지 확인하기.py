# 입력 받기
word = input()

# 단어를 뒤집은 문자열 생성
reversed_word = word[::-1]

# 팰린드롬 여부 확인
if word == reversed_word:
    print(1)
else:
    print(0)
# 
# 
# # 입력 받기
# word = input()
# 
# # 단어를 뒤집기 위한 변수 초기화
# reversed_word = ""
# 
# # for문을 사용하여 단어를 거꾸로 읽기
# for i in range(len(word) - 1, -1, -1):
#     reversed_word += word[i]
# 
# # 팰린드롬 여부 확인
# if word == reversed_word:
#     print(1)
# else:
#     print(0)
