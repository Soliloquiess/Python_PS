def solution(bin1, bin2):
    decimal_sum = int(bin1, 2) + int(bin2, 2)

    answer = bin(decimal_sum)[2:]

    return answer