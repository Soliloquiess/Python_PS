def solution(array):
    counts = {}
    for num in array:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    max_count = 0
    mode = []
    for num, cnt in counts.items():
        if cnt > max_count:
            max_count = cnt
            mode = [num]
        elif cnt == max_count:
            mode.append(num)

    if len(mode) > 1:
        return -1
    else:
        return mode[0]
