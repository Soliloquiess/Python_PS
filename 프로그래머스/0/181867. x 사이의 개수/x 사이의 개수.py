def solution(myString):
    lengths = []
    count = 0
    
    for ch in myString:
        if ch == 'x':
            lengths.append(count)
            count = 0
        else:
            count += 1
    lengths.append(count)  # 마지막 구간 길이 추가
    
    return lengths

#def solution(myString):
#    result = []
#    for s in myString.split("x"):
#       result.append(len(s))
#    return result
