def solution(i, j, k):
    count = 0
    k = str(k)
    
    for num in range(i, j+1):
        for ch in str(num):
            if ch == k:
                count += 1
    
    return count
