import sys
#sys.stdin=open("input.txt", "rt")
num, m=map(int, input().split())

def solution(num,m):
    num=list(map(int, str(num))) #string으로 바꾸면 하나하나 스트링으로 바꿈.
    #그리고 하나하나 접근  가능
    stack=[]
    for x in num:
        while stack and m>0 and stack[-1]<x:
            #스택이 비어있으면 거짓, 비어있지 않으면 참.  while stack 이건 비어있지 않았다는 뜻
            # while stack 이렇게만 쓰면 비어있지 않으면 참 , 비어있으면 거짓이 됨.
            #m은 0보다 커야 그 수를 pop시켜서 제외시킴.
            #이 부분은 스택에 들어간 수(맨 위 자료)가 나보다 작으면 꺼냄.
            #빼낼수만 있다면 계속 뺴냄
            stack.pop()#꺼내는 pop 시킴.
            m-=1        #하나 빼냈으니까 하나 감소시켜줘야 자기 앞에숫자가 나보다 작으면 -1로 팝시켜서 줄여준다.
        stack.append(x) #자기 앞에꺼 다 없에면 자기가 들어가야.(x) 앞의 자료 다 제거하고 넣어줌.
    if m!=0:        #다 지우지 못하는 경우
        stack=stack[:-m]       #스택 자료 새로 갱신
        # stack=stack[:-m]  이렇게 쓰면 맨 앞에서 m자료 전 까지 잘라버리고 뒤는 날려버림(뒤의 m개의 자료들 다 날아감)
        #뒤쪽의 m개의 자료가 날아간다.
    res=''.join(map(str, stack))
    #스트링을 조인시키는거. 맵 이용해서 스택을 string으로 변환(스택에 하나하나 정수라)

    # print(res)
    return res;

print(solution(num,m));


#리스트 이용하면
#list.pop하면 젤 뒤 빠지고
#list.append하면 젤 뒤 들어가고
#그래서 알아서 스택이 된다.

