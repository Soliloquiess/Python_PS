import sys
# sys.stdin=open("input.txt", "r")
a=input()
stack=[]
def solution(a):
    res = ''  # 출력을 res에 할 거
    for x in a:
        if x.isdecimal(): #x가 숫자인지 보는거. 10진수인지 확인하는건 isdigit과 isdecimal 2개가 있따.x가 10진수면 참
            res+=x        #res에 넣어서 출력
        else:               #그게 아니면 연산자.
            if x=='(':      #x가 여는 괄호면 스택에 넣어줌.
                stack.append(x)
            elif x=='*' or x=='/':  #연산자가 *이거나 /면 연산 우선순위 같으므로 연산 빠른애들만 뺴내는거
                while stack and (stack[-1]=='*' or stack[-1]=='/'):#스택이 비어있으면 안됨.

                #while stack 이건 스택이 비어있지 않다는 거 스택의 최상단 stack[-1]. 연산 우선순위 같으면 왼쪽부터
                #나눗셈 곱하기는 먼저 처리(우선순위 높으므로)
                #팝해서 먼저 처리.

                    res+=stack.pop()
                stack.append(x) #x들어가 줘야

            elif x=='+' or x=='-':  #x가 더하기 또는 빼기면 자기보다 스택 있는거들은 다 빠름.
                while stack and stack[-1]!='(':

                #일단 스택 빌떄까지 돌고 맨 최상위 자료가 ( 여는괄호 전 까지
                # 여는 괄호 만나면 멈추는거 (거짓되서)
                # 즉 elif x=='+' or x=='-':  여기는 괄호 안의 +,-를 의미하는 거
                #여는 괄호 전에 들어간 애들은 우선연산자가 나눗셈, 곱하기보다 우선됨.

                #여는 괄호 전까지 돌고 여는괄호 없으면 계속 쭉 진행. 여는괄호 만나면 아래 문 실행
                #여는 괄호 없으면 스택 다 뺴내겠지. 근데 있으면 멈추고 실행.
                    res+=stack.pop()

                stack.append(x) #이러면 더하기 뺴기도 처리한 거
            elif x==')':        #닫는 괄호 만나면 여는 괄호 만날떄 까지 감.(이거도 똑같음)

                #여는 괄호까지 만나며 그 괄호 안에 있는 연산자들을 다 뺴줌.
                #똑같이  res+=stack.pop() 해줌.

                while stack and stack[-1]!='(':

                    #만나서 멈춤(여는 괄호 만나서) 그래서 이  여는괄호 만나면 그사이 연산자 처리

                    res+=stack.pop()#
                stack.pop()     #   여는 괄호 출력 안하고 없애버리는 거.
    while stack:            #포문이 다 처리하고 스택에 남아있을 수도 있음. 그걸 처리해야됨.
        res+=stack.pop()
    # print(res)
    return res;

print(solution(a))




#스택에 있는 연산자 만나면 다 출력하자

