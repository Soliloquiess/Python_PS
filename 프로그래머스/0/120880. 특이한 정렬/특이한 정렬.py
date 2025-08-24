def solution(numlist, n):
    for i in range(len(numlist)):
        for j in range(i + 1, len(numlist)):
            if abs(numlist[i] - n) > abs(numlist[j] - n):
                numlist[i], numlist[j] = numlist[j], numlist[i]
            elif abs(numlist[i] - n) == abs(numlist[j] - n) and numlist[i] < numlist[j]:
                numlist[i], numlist[j] = numlist[j], numlist[i]
    return numlist


#def solution(numlist, n):
    # 정렬 기준: (거리, -값)  → 거리가 가까울수록 앞, 같으면 큰 값이 앞
#    return sorted(numlist, key=lambda x: (abs(x - n), -x))
