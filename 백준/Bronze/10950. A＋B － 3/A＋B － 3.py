n = int(input())

# for i in range(1,10):  # 1~9
#     print(n, '*', i, '=', n*i)

for i in range(1, n+1):
    a,b= map(int, input().split());
    c= a+b;
    print(c);
