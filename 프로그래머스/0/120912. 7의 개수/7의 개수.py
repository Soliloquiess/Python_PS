def solution(array):
    count = 0
    for num in array:
        while num > 0:
            if num % 10 == 7:   
                count += 1
            num //= 10         
    return count
