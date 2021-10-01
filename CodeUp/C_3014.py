# import sys

n = int(input())
array = list(map(int, input().split()))


def quick(array, start, end):
    if end-start <= 0:
        return array
    pivot = start
    left = start+1
    right = end

    while(left <= right):
        while(left <= end and array[pivot] >= array[left]):
            left += 1
        while(right > start and array[pivot] <= array[right]):
            right -= 1
        if(left > right):
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]

    quick(array, start, right-1)
    quick(array, right+1, end)


quick(array, 0, n-1)

for i in array:
    print(i, end=' ')