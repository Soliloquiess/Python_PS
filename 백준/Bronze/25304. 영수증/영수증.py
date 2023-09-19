t = int(input())
n = int(input())

sum = 0

for i in range(n):
    s = input().split()
    sum += int(s[0]) * int(s[1])

if sum == t:
    print("Yes")
else:
    print("No")
