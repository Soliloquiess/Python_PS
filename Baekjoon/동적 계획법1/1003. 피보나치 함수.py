t = int(input())

for _ in range(t):
    cnt_0 = [1, 0]
    cnt_1 = [0, 1]
    n = int(input())
    if n > 1:
        for i in range(n - 1):
            cnt_0.append(cnt_1[-1])
            cnt_1.append(cnt_0[-2] + cnt_1[-1])

    print(cnt_0[n], cnt_1[n])

#https://jiwon-coding.tistory.com/28?category=882771

# zero = [1, 0, 1]
# one = [0, 1, 1]
#
#
# def fibonacci(num):
#     length = len(zero)
#     if num >= length:
#         for i in range(length, num + 1):
#             zero.append(zero[i - 1] + zero[i - 2])
#             one.append(one[i - 1] + one[i - 2])
#     print('{} {}'.format(zero[num], one[num]))
#
#
# T = int(input())
#
# for _ in range(T):
#     fibonacci(int(input()))