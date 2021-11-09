import sys
#sys.stdin=open("input.txt", "r")
a=input()
b=input()

str1=[0]*52 #각각 str1,2,에 해싱(저번거처럼)
str2=[0]*52#처음엔 r1,r2 둘다 0으로 초기화

def solution(a,b):
    for x in a: #x가 알파벳 하나하나
        if x.isupper(): #대문자 소문자 구분하기 위해 이게 참이면 x라는 알파벳은 대문자.
            str1[ord(x)-65]+=1  #ord(x) 이게 아스키 넘버.
            #ord(x)-65 하면 대문자. 그게 +1됨.
        else:
            str1[ord(x)-71]+=1
            #소문자면 71 빼야 소문자 a가 26으로 해싱됨.
            # [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            #  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            #현 이런상태고 여기서 대문자에서 -71을 빼면 그 자리(소문자자리에) +1이 채워진다는 의미.
    for x in b:
        if x.isupper():
            str2[ord(x)-65]+=1
        else:
            str2[ord(x)-71]+=1
            #두번째 단어도 똑같이 해싱함.
    #if str1==str1 이렇게 해도 되긴 함.
    for i in range(52):
        if str1[i]!=str2[i]:
            #i가 0이면 대문자개수가 동일하냐, 1이면 대문자 b의 개수가 동일하냐 이렇게 물어서 아나그램 판별.
            # print("NO")
            return "NO"
            break
    else:
        # print("YES")
        return "YES"

print(solution(a,b));












