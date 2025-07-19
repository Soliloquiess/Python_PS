def solution(names):
    result = []
    for i in range(0, len(names), 5):
        result.append(names[i])
    return result

#def solution(names):
#    return [names[i] for i in range(0, len(names), 5)]
