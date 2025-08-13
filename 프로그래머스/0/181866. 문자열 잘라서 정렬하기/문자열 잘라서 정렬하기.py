def solution(myString):
    result = []
    for s in myString.split("x"):
        if s:            # 빈 문자열이면 건너뜀
            result.append(s)
    result.sort()        # 사전순 정렬
    return result


