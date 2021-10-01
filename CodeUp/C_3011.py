num=int(input())
arr=list(map(int,input().split()))
cnt=0
for i in range(num):
    change_flag=False
    for j in range(num-i-1):
        if arr[j]>arr[j+1]:
            temp=arr[j]
            arr[j]=arr[j+1]
            arr[j+1]=temp
            change_flag=True
    if change_flag:
        cnt+=1
print(cnt)


### 병신같이 짜서 이건 안됨.
# import sys
#
# n = int(sys.stdin.readline())
# array = list(map(int, sys.stdin.readline().split()))
# cnt = 0
#
# for i in range(n-1, 0, -1):
#     swap = 0
#     for j in range(i):
#         if (array[j] > array[j+1]):
#             array[j], array[j+1] = array[j+1], array[j]
#             swap += 1
#     cnt += 1
#     if swap == 1:
#         print(cnt)
#         break
#
#     else:
#         print(cnt-1);
# # a

# n = int(input())
# array = list(map(int, input().split()))
# cnt = 0
#
# for i in range(n-1, 0, -1):
#     swap = 0
#     for j in range(i):
#         if (array[j] > array[j+1]):
#             array[j], array[j+1] = array[j+1], array[j]
#             swap += 1
#     cnt += 1
#     if swap == 0:   #swap되는게 0이면 정렬이 이미 완료 된 것.
#         break
#
# print(cnt-1)
