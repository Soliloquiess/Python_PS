def solution(my_string, s, e):
    # s 이전 부분 + s~e 구간 뒤집기 + e 이후 부분
    return my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]


# def solution(my_string, s, e):
#     chars = list(my_string)  # 문자열을 문자 리스트로 변환

#     # s와 e 인덱스 사이를 투 포인터로 뒤집기
#     while s < e:
#         chars[s], chars[e] = chars[e], chars[s]
#         s += 1
#         e -= 1

#     return ''.join(chars)  # 리스트를 다시 문자열로 합치기