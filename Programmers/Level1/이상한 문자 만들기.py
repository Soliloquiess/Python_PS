# def solution(s):
#     s_list = list(s)
#
#     for i in range(len(s_list)):
#         if i % 2 == 0:
#             s_list[i] = s_list[i].upper()
#         elif i % 2 == 1:
#             s_list[i] = s_list[i].lower()
#
#     answer = "".join(s_list)
#     return answer
#
# print(solution("try hello world"))
# 위는 실패 (너무 단순하게 생각) 짝수 대문자 홀수 대문자긴 하지만 공백을 고려해야 한다.


def solution(s):
    s_split = s.split(" ") #공백 기준으로 자름.

    for k in range(len(s_split)):
        s_list = list(s_split[k])   #여기서 공백 나눠진 단어의 각 요소들을 s_list에 넣는다.

        for i in range(len(s_list)):
            if i % 2 == 0:
                s_list[i] = s_list[i].upper()
            elif i % 2 == 1:
                s_list[i] = s_list[i].lower()
        s_split[k] = "".join(s_list)
    answer = " ".join(s_split)  #위에서 s_split[k]에 각 단어 바뀐거 넣어주고 그 바뀐 요소들을 answer에 넣어준다.
    return answer

print(solution("try hello world"))
#그래서 공백을 기준으로 나눈뒤에 각 문자열에서 각 문자열의 인덱스를 기준으로 진행



# def solution(s):
#     s_list = list(s)
#
#     for i in range(len(s_list)):
#         if i % 2 == 0:
#             s_list[i] = s_list[i].upper()
#         elif i % 2 == 1:
#             s_list[i] = s_list[i].lower()
#
#     answer = "".join(s_list)
#     return answer
#
# print(solution("try hello world"))
# 이거는 공백 신경 안쓰고 짝홀(그니까 공백포함해서 짝수번째 계산한거.)