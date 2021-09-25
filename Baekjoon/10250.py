T = int(input())

for i in range(T):
    H, W, N = list(map(int, input().split()))

    if (N % H == 0):
        Y = H * 100
        X = N // H
    else:
        Y = (N % H) * 100;
        X = (N // H) + 1;

    print(Y + X)

# t = int(input())
#
# for i in range(t):
#     h, w, n = map(int, input().split())
#     num = n // h + 1
#     floor = n % h
#     if n % h == 0:  # h의 배수이면,
#         num = n // h
#         floor = h
#     print(f'{floor * 100 + num}')
