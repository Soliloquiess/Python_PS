def solution(numLog):
    answer = ''
    
    for i in range(1, len(numLog)):
        diff = numLog[i] - numLog[i - 1]
        
        if diff == 1:
            answer += 'w'  # 수에 1을 더한 경우
        elif diff == -1:
            answer += 's'  # 수에 1을 뺀 경우
        elif diff == 10:
            answer += 'd'  # 수에 10을 더한 경우
        elif diff == -10:
            answer += 'a'  # 수에 10을 뺀 경우
    
    return answer
