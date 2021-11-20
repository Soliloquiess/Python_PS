N = int(input())

M = []

for i in range(N):
    M.append(int(input()))

# Bubble Sort
for i in range(len(M)):
    for j in range(len(M)):
        if M[i] < M[j]:
            M[i], M[j] = M[j], M[i]

for n in M:
    print(n)
#위는 버블정렬
# https://0ver-grow.tistory.com/412

# N = int(input())
# M = []
#
# for i in range(N):
#     M.append(int(input()))
#
# # Insert Sort
# for i in range(1, len(M)):
#     while (i > 0) & (M[i] < M[i - 1]):
#         M[i], M[i - 1] = M[i - 1], M[i]
#
#         i -= 1
#
# for n in M:
#     print(n)
# #이건 선택정렬
#
#sort사용

# x = int(input())
# num_list = []
# for i in range(x):  #len 안써야됨(int로 들어왔기 떄문)
#     num_list.append(int(input()))
# num_list1 = sorted(num_list)
# for i in range(len(num_list)):
#     print(num_list1[i])