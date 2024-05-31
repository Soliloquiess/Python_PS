height=int(input())


for i in range(height):
    for j in reversed(range(height)):# for(int i= n-1; i=0 ; i--)와 같다고 보면 될듯.
        if j > i:
            print(' ', end='')
        else:
            print('*', end='')

    print();

#
# n= int(input())
#
# for i in range(n):
#     for j in range(n):
#         if(j>i):
#             print(' ', end='')
#
#     for k in range(n):
#         if(k< i+1):
#             print('*', end='')
#     print()