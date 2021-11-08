import sys
#sys.stdin=open("input.txt", "r")
s=input()
stack=[]

def solution(s):
    cnt=0
    for i in range(len(s)):
        if s[i]=='(':   #여는 괄호인지 보는 거.
            stack.append(s[i])  #여는 괄호면 스택에 넣어준다.
        else:           #그게 아니면 닫는 괄호
            stack.pop()#굳이 양쪽에서 다 할필요 없이 여기서 stack.pop 해도 된다.
            #근데 if else에서 다 pop하는거 미리 팝하고 개수세고 해도 되긴함.
            # 근데  갠적으로는 이거보다 밑에서 주석친 pop 방법이 더 이해는 잘 되는 듯.

            if s[i-1]=='(': #바로 앞의 지점 이게 여는괄호인지 확인(닫는 괄호 앞에 바로 여는 괄호이면 열고 닫고가 바로 있으므로 레이저
                #stack.pop()    #레이저면 팝 시킴.
                cnt+=len(stack) #레이저 하면 앞에있던 여는 괄호가 다 쇠막대기 되는거
            else:               #그게 아니면 닫는괄호 만난거고  1 더하기

                # stack.pop()
                cnt+=1          #그 앞에 지점에 여는게 아니면 닫는거일것(쇠막대기의 끝)
                #이 cnt+=1은 마지막 조각을 세는거 그리고 이떄는 pop하면서 cnt더함(맨 마지막 레이저 이후)
    # print(cnt)
    return cnt;

print(solution(s));