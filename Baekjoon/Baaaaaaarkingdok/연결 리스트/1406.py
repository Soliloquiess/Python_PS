from sys import stdin

d1 = list(stdin.readline().rstrip())
d2 = []

N = int(stdin.readline().rstrip())
c = len(d1)

for i in range(N):
    a = stdin.readline().rstrip()
    if (a == 'L'):
        if d1:
            d2.append(d1.pop())
    elif (a == 'D'):
        if d2:
            d1.append(d2.pop())
    elif (a == 'B'):
        if d1:
            d1.pop()
    else:
        d1.append(a[2])

print(''.join(d1+list(reversed(d2))))