def solution(num_list):
    if len(num_list) >= 11:
        total = 0
        for num in num_list:
            total += num
        return total
    else:
        product = 1
        for num in num_list:
            product *= num
        return product
