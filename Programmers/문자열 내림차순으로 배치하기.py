# def solution(s):
#     return (''.join(sorted(s)[::-1]))
#
# print(solution("Zbcdefg"))


# def solution(s):
#     return (''.join(reversed(sorted(s))))
#
# def solution(s):
#     return ''.join(sorted(s, reverse=True))

s = 'abcde'
s_list = list(s)  # reverse 함수를 사용하기 위해 문자열을 list로 치환
s_list.reverse()  # reverse 함수를 사용해 문자열 리스트를 거꾸로 뒤집음

print(''.join(s_list))  # 거꾸로 뒤집어진 리스트를 연결해서 출력

#
# s = 'abcde'
# print(''.join(reversed(s)))  # 'edcba'
#
# s = 'abcde'
# print(s[::-1])  # 'edcba'