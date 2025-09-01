def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    
    answer = []
    for value in emergency:
        rank = sorted_emergency.index(value) + 1
        answer.append(rank)
        
    return answer
