a = int(input())
b = int(input())

print(a*(b%10),
      a*((b//10)%10),
      a*(b//100),
      a*b,sep="\n");


# a = int(input())
# b = input()
# for i in range(2, -1, -1):
#     print(a * int(b[i]))
# print(a*int(b))