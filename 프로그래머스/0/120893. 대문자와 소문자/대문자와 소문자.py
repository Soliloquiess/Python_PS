def solution(my_string):
    result = ""
    for ch in my_string:
        if ch.islower():   
            result += ch.upper()
        else:             
            result += ch.lower()
    return result
