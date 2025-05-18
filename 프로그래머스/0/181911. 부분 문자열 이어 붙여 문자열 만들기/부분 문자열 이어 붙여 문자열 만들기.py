def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        s, e = parts[i]               # 부분 문자열의 시작과 끝 인덱스
        answer += my_strings[i][s:e+1]  # 해당 범위 문자열 추출 후 이어 붙임
    return answer
