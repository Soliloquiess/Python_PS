height=int(input())


for i in range(int(height/2) +1):

    for j in range(int(height/2)-i):
        print(' ', end='');

    for j in range(i*2+1):
        print('*', end='')
    print()