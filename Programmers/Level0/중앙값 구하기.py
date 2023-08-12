def solution(n):
    even_numbers = sorted(n)  # 리스트를 정렬하여 even_numbers 변수에 할당
    # print(even_numbers);
    # even_numbers = [num for num in range(n, m + 1) if num % 2 == 0]
    centerIndex = len(even_numbers) // 2

    if len(even_numbers) % 2 == 1:
        center_value = even_numbers[centerIndex]
    else:
        center_value = (even_numbers[centerIndex] + even_numbers[centerIndex - 1]) / 2
    print(f"{center_value}")
    return center_value

print(solution([1, 2, 7, 10, 11]))