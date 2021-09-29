
size,course = map(int, input().split())
d = [0]*size
result = [0]*size

for i in range(course):
    s, e, u = map(int, input().split())
    d[s-1] = d[s-1]+u
    d[e] = d[e]-u

start = 0
for i in range(size):
    result[i] = start+d[i]
    start = result[i]
    print(d[i], end=' ')
print(' ')

for i in range(size):
    print(result[i], end=' ')