def solution(num, total):
    mid = total / num
    start = int(mid - (num - 1) / 2)
    
    answer = []
    for i in range(num):
        answer.append(start + i)
    return answer