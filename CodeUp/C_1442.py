import sys

n = int(input())
array = [int(input()) for _ in range(n)]

for i in range(n-1):
    min = i
    for j in range(i+1, n):
        if(array[min] > array[j]):
            min = j
    if (min != i):
        array[i], array[min] = array[min], array[i]

for i in array:
    print(i)