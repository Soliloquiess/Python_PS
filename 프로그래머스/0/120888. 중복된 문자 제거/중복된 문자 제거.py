def solution(my_string):
    seen = set()  
    result = ""
    
    for ch in my_string:
        if ch not in seen:
            result += ch
            seen.add(ch)
    
    return result
