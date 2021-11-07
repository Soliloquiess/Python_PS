import sys
from collections import deque
# sys.stdin=open("input.txt", "r")
need=input()
n=int(input()) #플랜 개수
for i in range(n):
    plan=input()
    dq=deque(need)  #매번 현수 플랜 읽고 필수과목으로 초기화
    for x in plan:  #플랜 하나하나 검증. (x가 dq에 있는게 아니라 plan에 있는 과목 도는거)
        if x in dq: #수업 과목하나하나 x가 접근하는거
            if x!=dq.popleft(): #덱 안에 x가 있냐 없냐 확인(덱 안에 있어야 필수과목이므로) 젤 앞에서 꺼낸 자료와 같지 않으면 순서에 어긋남.
                #x가 젤 앞에서 꺼낸 필수과목의 맨 앞 자료와 현재과목이 일치하지 않으면 순서 어긋남.
                #만약 덱 안에 있는데 x와 덱에서 popleft한 과목이 다르면 바로 no 출력하고 break;
                print("#%d NO" %(i+1))  #no라고 찍음.(i가 0부터 도니까 +1 햊줌)
                break   #no 찍고 브레이크 하면 돌다 멈춤
    else:       #정상적으로 끝남 = 순서는 다 통과
        #근데 순서 다 통과해도 필수과목 다 넣었는지 확인해야
        if len(dq)==0:  #덱에 남아있으면 그 자료는 필수과목 아님(팝 못시킴). 플랜에 있어야 팝시킴.
            #0이면 잘 짠거라 yes 출력
            print("#%d YES" %(i+1))
        else:
            #큐에 과목 남아있으면 필수과목 설계에 넣지 않은거
            #즉 cba 인데 만약 cbqwe이면 순서는 다 맞는데 덱에 a가 남아있어서 통과 못하는 거.
            print("#%d NO" %(i+1))
