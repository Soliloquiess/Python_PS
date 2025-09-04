def solution(age):
    age_map = {'0': 'a', '1': 'b', '2': 'c', '3': 'd', '4': 'e',
               '5': 'f', '6': 'g', '7': 'h', '8': 'i', '9': 'j'}
    
    age_str = str(age)
    result = ""
    
    for char in age_str:
        result += age_map[char]
        
    return result

# def solution(age):
#     age_str = str(age)
#     result=""
    
#     for char in age_str:
#         result += chr(ord(char) + 49)
        
#     return result
