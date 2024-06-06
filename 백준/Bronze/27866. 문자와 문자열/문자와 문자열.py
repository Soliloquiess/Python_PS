# 입력 받기
S = input().strip() #strip은 공백 제거
i = int(input().strip())

# i번째 글자 출력 (파이썬 인덱스는 0부터 시작하므로 i-1을 사용)
print(S[i-1])


# 입력 받기
#S = input().strip()
#i = int(input().strip())

# 반복문을 사용하여 i번째 문자를 찾기
#position = 1  # 문자열의 1번째 문자부터 시작 (1-based indexing)
#for char in S:
#    if position == i:
#        print(char)
#        break
#    position += 1

