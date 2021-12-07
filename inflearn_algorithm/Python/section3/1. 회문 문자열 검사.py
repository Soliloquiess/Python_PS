import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
def solution(n):
    for i in range(1, n+1):
        str=input()             #str 입력
        str=str.upper()         #str 전부 대문자로 만들고
        for j in range(0,len(str)//2):        #반복문은 반만 돌아도 됨.
            if str[j]!=str[-1-j]:           #str[j]부분과 맨 뒷자리 같은지 확인 다르면 NO출력
                                            #-j하는건 어차피 j가 인덱스 0부터 시작하므로
                print("#%d NO" %i)
                break
        else:
            print("#%d YES" %i)


print(solution(n))



# <다른코드>
# import sys
# sys.stdin=open("input.txt", "r")
# n=int(input())
# for i in range(n):
#     str=input()
#     str=str.upper()
#     if str==str[::-1]:
#         print("#%d YES" %i)
#     else:
#         print("#%d NO" %i)