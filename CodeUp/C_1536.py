def f():
    min = li[0]
    for i in range(a):
        if min > li[i]:
            min = li[i]
    return min


a = int(input())
li = list(map(int, input().split()))
print(f())


# def f():
#     min = li[0]
#     #for i in range(a)를 사용하지 않고 i안에 리스트 요소를 넣어서도 풀 수 있다.
#
#
#     for i in li:
#         if i < min:
#             min = i
#     return min
#
#
# a = int(input())
# li = list(map(int, input().split()))
# print(f())