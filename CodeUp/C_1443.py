import sys

n = int(input())
array = [0]*n

for i in range(n):
    array[i] = int(input())

for i in range(1, n):
    for j in range(i, 0, -1):
        if(array[j] < array[j-1]):
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

for i in array:
    print(i)