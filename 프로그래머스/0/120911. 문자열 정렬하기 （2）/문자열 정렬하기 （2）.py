def solution(my_string):
    lower_str = my_string.lower()
    
    sorted_chars = sorted(lower_str)
    
    answer = ''.join(sorted_chars)
    return answer
