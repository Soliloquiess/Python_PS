def hanoi_tower(n, start, end):
    if n == 1:
        print(start, end)
        return

    hanoi_tower(n - 1, start, 6 - start - end)  # 1단계
    print(start, end)  # 2단계
    hanoi_tower(n - 1, 6 - start - end, end)  # 3단계


n = int(input())
print(2 ** n - 1)
hanoi_tower(n, 1, 3)

# https://study-all-night.tistory.com/6

# hanoi function def
# def hanoi(n,a,b,c):
#     if n==1:
#         move.append([a,c])
#     else:
#         hanoi(n-1,a,c,b)
#         move.append([a,c])
#         hanoi(n-1,b,a,c)
#
# move = [] # 이동 경로를 담을 list
# hanoi(int(input()),1,2,3) # function 실행
#
# print(len(move)) # 이동 횟수
# print("\n".join([' '.join(str(i) for i in row) for row in move])) # 이동 경로 출력


# Recursive Python function to solve the tower of hanoi

# def TowerOfHanoi(n, source, destination, auxiliary):
#     if n == 1:
#         print
#         "Move disk 1 from source", source, "to destination", destination
#         return
#     TowerOfHanoi(n - 1, source, auxiliary, destination)
#     print
#     "Move disk", n, "from source", source, "to destination", destination
#     TowerOfHanoi(n - 1, auxiliary, destination, source)
#
#
# # Driver code
# n = 4
# TowerOfHanoi(n, 'A', 'B', 'C')
# # A, C, B are the name of rods
#
# # Contributed By Dilip Jain