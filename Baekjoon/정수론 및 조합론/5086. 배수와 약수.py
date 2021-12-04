while (True):
    a, b = list(map(int, input().split()))

    # 0, 0
    if (a + b == 0):
        break

    # case 1
    if (a < b):
        if (b % a == 0):
            print('factor')
        else:
            print('neither')
    elif (a > b):
        if (a % b == 0):
            print('multiple')
        else:
            print('neither')
#https://hwiyong.tistory.com/352


# while True:
#     a, b = map(int, input().split())
#     if a == 0 and b == 0:
#         break
#     if b % a == 0:
#         print('factor')
#     elif a % b == 0:
#         print('multiple')
#     else:
#         print('neither')

#https://pacific-ocean.tistory.com/146

