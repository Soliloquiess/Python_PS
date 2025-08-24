def solution(array, n):
    closest = array[0] 
    min_diff = abs(array[0] - n)
    
    for num in array[1:]:
        diff = abs(num - n)
        if diff < min_diff:
            min_diff = diff
            closest = num
        elif diff == min_diff and num < closest:
            closest = num
    
    return closest
