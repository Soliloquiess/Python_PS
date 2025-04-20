def solution(l, r):
    from collections import deque
    
    result = []
    queue = deque(['5'])  

    while queue:
        num_str = queue.popleft()
        num = int(num_str)
        
        if num > r:
            continue
        if num >= l:
            result.append(num)
        
        queue.append(num_str + '0')
        queue.append(num_str + '5')
    
    return sorted(result) if result else [-1]
