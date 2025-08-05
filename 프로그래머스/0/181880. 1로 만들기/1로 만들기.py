def solution(num_list):
    total = 0
    for num in num_list:
        while num > 1:
            num //= 2
            total += 1
    return total
