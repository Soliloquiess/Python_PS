def solution(myString, pat):
    myString = myString.lower()
    pat = pat.lower()
    
    for i in range(len(myString) - len(pat) + 1):
        if myString[i:i+len(pat)] == pat:
            return 1
    return 0
