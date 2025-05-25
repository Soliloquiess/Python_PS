def solution(my_string):
    answer = [0] * 52  # 대문자 26개 + 소문자 26개
    
    for ch in my_string:
        if 'A' <= ch <= 'Z':
            idx = ord(ch) - ord('A')  # 0~25
        else:
            idx = ord(ch) - ord('a') + 26  # 26~51
        answer[idx] += 1
    
    return answer
