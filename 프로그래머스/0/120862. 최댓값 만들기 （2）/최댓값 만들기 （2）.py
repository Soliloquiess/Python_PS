def solution(numbers):
    numbers.sort()
    
    product1 = numbers[-1] * numbers[-2]
    product2 = numbers[0] * numbers[1]
    
    if product1 > product2:
        return product1
    else:
        return product2
