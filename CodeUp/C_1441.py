n = int(input());
a=[]
for i in range(0,n):
    a.append(int(input()));

for i in range(0, n):
    for j in range (0, n-1):
        if(a[j]>a[j+1]):
            temp=a[j];
            a[j] = a[j+1];
            a[j+1]=temp;

for i in range(0,n):
    print(a[i])
# n = int(input())
# array = [int(input()) for _ in range(n)]
#
# end = n-1
#
# while(end > 0):
#     swap = 0
#     for j in range(end):
#         if (array[j] > array[j+1]):
#             array[j], array[j+1] = array[j+1], array[j]
#             swap = j
#         end = swap
#
# for i in array:
#     print(i)