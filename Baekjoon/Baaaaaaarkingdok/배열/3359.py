A = int(input())
B = int(input())
C = int(input())
T = A * B * C
List = [0] * 10
while T != 0:
    List[T % 10] += 1
    T //= 10
for i in List:
    print(i)