# 튜플
def solution(s):
    answer = []
    # 입력받은 s 문자열의 괄호와 끝 괄호를 제거하고 리스트 형태로 변환
    s_list = s.replace('{', '').replace('}}', '').split('},')
    # 각 원소의 길이를 기준으로 정렬
    s_list.sort(key=len)
    # s_list의 문자열을 각각 접근
    for string in s_list:
        # 문자열을 정수화 하고 리스트화 하여 nubmers에 넣기
        numbers = list(map(int, string.split(',')))
        # numbers의 숫자를 하나씩 접근하며 답 리스트에 없는 경우에만 append
        for number in numbers:
            if number not in answer:
                answer.append(number)
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))
print(solution("{{123}}"))
print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
# def solution(s):
#     answer = []
#     s = s[2:-2]
#     s = sorted(s.split("},{"), key = lambda x: len(x))
#
#     for i in s:
#         i_ = i.split(',')
#         for j in i_:
#             if int(j) not in answer:
#                 answer.append(int(j))
#     return answer