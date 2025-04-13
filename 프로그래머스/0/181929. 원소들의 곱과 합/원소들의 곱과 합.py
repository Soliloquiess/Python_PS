def solution(num_list):
    total_mul = 1  # 곱
    total_sum = 0  # 합
    for num in num_list:
        total_mul *= num
        total_sum += num
    return 1 if total_mul < total_sum ** 2 else 0
