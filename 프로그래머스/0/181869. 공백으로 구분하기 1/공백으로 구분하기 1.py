def solution(my_string):
    result = []
    word = ""
    for ch in my_string:
        if ch == " ":
            result.append(word)
            word = ""
        else:
            word += ch
    result.append(word) 
    return result



#def solution(my_string):
#    return my_string.split(" ")
