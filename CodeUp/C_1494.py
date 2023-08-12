n, k = map(int, input().split())

d = [0] * n

for _ in range(k):
    s, e, u = map(int, input().split())
    d[s-1] += u
    if e < n:
        d[e] -= u

sum_list = []
sum = 0
for i in range(n):
    sum += d[i]
    sum_list.append(sum)

print(*d)
print(*sum_list)
