n= int(input())

# for _ in range(int(input())):

for _ in range(n):
    # a, b = list(map(list, input().split()))
	a, b = map(list, input().split())
	a.sort()
	b.sort()
	if a == b:
		print('Possible')
	else:
		print('Impossible')

