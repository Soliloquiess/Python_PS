import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
a=list(map(int, input().split()))
ave=sum(a)/n #sum이라는 함수는 리스트에 있는 모든 함수를 합해줌.
ave=ave+0.5 #평균에 반올림. 그리고 round함수는 half_even이라 안 정확 할수도 있다하니 우리는 0.5를 더하는 방식으로 쓰자.
ave=int(ave)
#min=2147000000
min=float('inf'); #float 형의 최대값을 넣어줄 수 있따.

#min=float('-inf'); #이렇게 하면 float 형의 최소값을 넣어줄 수 있따.
for index, x in enumerate(a):   #인덱스 = 학생번호 , x= 성적
    #enumerater(a) 하면 a라는 리스트에 값이 들어있을떄
    #a라는 리스트 탐색시 index에는 인덱스 값(번호)를 반환 , x는 리스트에 있는 값을 넣음.
    #리스트의 인덱스 값과 리스트의 밸류값(실제 값을) 대응해 주는게 enumerate();
    tmp=abs(x-ave)  #평균과 실제 학생과의 거리 구해야.
    if tmp<min:
        min=tmp
        score = x;#거리값의 같았을때는 큰 점수
        res=index+1   #idx가 진짜 점수고 거기에 +1(인덱스니까)
    elif tmp==min:  #같은 거리가 나왔을 떄는 #점수가 큰 학생이 답임
        if x>score:#근데 같은 점수 들어온다 치면 점수가 클때만 이게 참이므로 같은 점수가 와도 이 구문은 실행 안함.
            score=x
            res=index+1
print(ave, res)