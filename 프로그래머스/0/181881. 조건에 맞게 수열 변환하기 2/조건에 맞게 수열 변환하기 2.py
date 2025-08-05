def solution(arr):
    x = 0
    while True:
        changed = False
        next_arr = []

        for num in arr:
            if num >= 50 and num % 2 == 0:
                next_arr.append(num // 2)
            elif num < 50 and num % 2 == 1:
                next_arr.append(num * 2 + 1)
            else:
                next_arr.append(num)

        if next_arr == arr:
            return x
        
        arr = next_arr
        x += 1
