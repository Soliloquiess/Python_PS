N = int(input())
A = []
for i in range(N) :
    A.append(input())


for a in range(N-1) :
    flag = 0
    for b in range(N-1) :
        if A[b] > A[b+1] :
            A[b], A[b+1] = A[b+1], A[b]
            flag = 1
            print(A)

    if flag == 0 :
        break


for i in range(N-1) :
    if(A[0]=='0'):
        A.append(A.pop(0));
    else:
        break;


print(A)


# def left_right(arr):
#     tmp = int(input('입력하시오 :'))
#     if tmp == 1:
#         return arr
#     else:
#         return list(reversed(arr))
# print(left_right([1,0,4,5,2,0,0,0]))



# def left_right(arr):
#     tmp = int(input('입력하시오 :'))
#     if tmp == 1:
#         return arr
#     else:
#         return list(reversed(arr))