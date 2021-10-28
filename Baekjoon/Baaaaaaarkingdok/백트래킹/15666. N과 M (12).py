n, m = map(int, input().split())
num_list = list(map(int, input().split()))
num_list = list(set(num_list))
num_list.sort()

a = [0 for i in range(m)]

def go(idx, selected, m):
    if selected == m:
        print(' '.join(map(str, a)))
        return
    if idx == len(num_list):
        return
    a[selected] = num_list[idx]
    go(idx, selected + 1, m)
    a[selected] = 0
    go(idx + 1, selected, m)

go(0, 0, m)
#   https://hjp845.tistory.com/88?category=859229


# from itertools import combinations_with_replacement
#
# n,m=map(int,input().split())
#
# a=list(map(int,input().split()))
# a.sort()
# a=list(combinations_with_replacement(a, m))
#
# a=sorted(list(set(a)))
#
# for i in a:
#     print(*i)

# https://it-garden.tistory.com/164?category=845077