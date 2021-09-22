m=input();
n=input()

arr = list(n)
sum =0;
arr= list(map(int, arr));

for i in range(len(n)):
    sum += arr[i];

print(sum)


# a = int(input())
# n = list(input())
# sum = 0
# for i in n:
#     sum += int(i)
# print(sum)