def solution(my_string, num1, num2):
    s = list(my_string)             
    s[num1], s[num2] = s[num2], s[num1] 
    result = ''.join(s)
    return result
#    return ''.join(s)             
