# 입력 받기
input_string = input().strip()

# 문자열을 공백 기준으로 분리하여 단어 리스트 생성
words = input_string.split()

# 단어의 개수를 셈
word_count = len(words)

# 결과 출력
print(word_count)


# 첫번째 풀이
# word = input().split()
# print(len(word))

# 두번째 풀이
#print(len(input().split()))