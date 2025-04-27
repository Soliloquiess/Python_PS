def solution(a, b, c, d):
    nums = [a, b, c, d]
    counts = {}
    
    # 각 숫자가 몇 번 나왔는지 세기
    for num in nums:
        counts[num] = counts.get(num, 0) + 1

    # (숫자, 등장 횟수) 리스트 만들고 등장 횟수 기준으로 정렬
    items = sorted(counts.items(), key=lambda x: -x[1])

    if len(counts) == 1:
        # 모두 같은 경우
        p = items[0][0]
        return 1111 * p
    elif len(counts) == 2:
        if items[0][1] == 3:
            # 세 개 같은 경우
            p = items[0][0]
            q = items[1][0]
            return (10 * p + q) ** 2
        else:
            # 두 개씩 같은 경우
            p = items[0][0]
            q = items[1][0]
            return (p + q) * abs(p - q)
    elif len(counts) == 3:
        # 두 개 같은 경우
        # (items 리스트에서 등장 횟수가 2인 숫자를 제외하고 나머지 두 수 q, r을 뽑음)
        for num, cnt in items:
            if cnt == 2:
                p = num
            else:
                q, r = [n for n, c in items if c == 1]
        return q * r
    else:
        # 모두 다른 경우
        return min(nums)
