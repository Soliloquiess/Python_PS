import sys
sys.stdin=open("input.txt", "r")
a=input()
stack=[]
for x in a:
    if x.isdecimal():#숫자인지 확인
        stack.append(int(x))# stack 이라서 넣을 떄 int화 시켜서 넣어야 한다!(중요)
    else:
        if x=='+':
            n1=stack.pop()
            n2=stack.pop()      #2개 꺼내야 하므로(연산 하려면 당연히 숫자 2개 꺼내야)
            stack.append(n2+n1) #둘이 더한값 넣어줌.
        elif x=='-':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2-n1)
        elif x=='*':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2*n1)
        elif x=='/':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2/n1)

            #그냥 사칙연산 스택에 있는거 해주는거.

print(stack[0])
#이거 다 하고나면 스택에 단 하나 자료 남는데 그 0번자료 출력하면 됨.