def solution(a, b, c, d):
    nums = [a, b, c, d]
    counts = {}
    
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    items = sorted(counts.items(), key=lambda x: -x[1])

    if len(counts) == 1:
        p = items[0][0]
        return 1111 * p
    elif len(counts) == 2:
        if items[0][1] == 3:
            p = items[0][0]
            q = items[1][0]
            return (10 * p + q) ** 2
        else:
            p = items[0][0]
            q = items[1][0]
            return (p + q) * abs(p - q)
    elif len(counts) == 3:
        for num, cnt in items:
            if cnt == 2:
                p = num
            else:
                q, r = [n for n, c in items if c == 1]
        return q * r
    else:
        return min(nums)
