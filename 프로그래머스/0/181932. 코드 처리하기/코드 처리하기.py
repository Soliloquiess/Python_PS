def solution(code):
    answer = []
    mode = 0

    for idx, char in enumerate(code):
        if char == '1':
            mode = 1 - mode  # mode 전환
        else:
            if (mode == 0 and idx % 2 == 0) or (mode == 1 and idx % 2 == 1):
                answer.append(char)

    return ''.join(answer) if answer else 'EMPTY'


# def solution(code):
#     mode = 0  # 시작 시 mode는 0
#     ret = ""  # 최종 결과를 저장할 변수

#     for idx, char in enumerate(code):
#         if mode == 0:
#             if char != "1":
#                 if idx % 2 == 0:  # mode가 0이고, idx가 짝수일 때만
#                     ret += char  # 문자 추가
#             else:
#                 mode = 1  # mode를 1로 변경

#         elif mode == 1:
#             if char != "1":
#                 if idx % 2 == 1:  # mode가 1이고, idx가 홀수일 때만
#                     ret += char  # 문자 추가
#             else:
#                 mode = 0  # mode를 0으로 변경

#     return ret if ret != "" else "EMPTY"  # 결과가 빈 문자열이면 "EMPTY" 반환


# # 테스트
# print(solution("abc1abc1abc"))  # "acbac"
