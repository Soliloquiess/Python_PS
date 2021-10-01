n=int(input())
number=map(int,input().split())
k=int(input())
number=list(number)

def f(k):
    flag=False
    for i in range(len(number)):
        if number[i]==k:
            print(i+1)
            flag=True
            break
    if not flag:
        print(-1)
f(k)


# def f():
# 	n = int(input())
# 	my_array = list(map(int, input().split()))
# 	k = int(input())
# 	for index, value in enumerate(my_array):
# 		if value == k:
# 			return index + 1
# 	return -1
#
#
# print(f())

