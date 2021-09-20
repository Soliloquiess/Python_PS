n= int(input())

for i in range(n):
    for j in range(n):
        if(j>i):
            print(' ', end='')

    for k in range(n):
        if(k< i+1):
            print('*', end='')
    print()