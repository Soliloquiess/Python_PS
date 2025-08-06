def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    
    for i in range(len(myString) - len(pat) + 1):
        if myString[i:i+len(pat)] == pat:
            return 1
    return 0

#def solution(myString, pat):
#    return 1 if pat.lower() in myString.lower() else 0