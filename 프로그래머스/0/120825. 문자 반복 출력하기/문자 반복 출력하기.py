def solution(my_string, n):
    result = ""
    for ch in my_string:
        for _ in range(n):   
            result += ch
    return result
