import sys
#sys.stdin=open("input.txt", "r")
n=int(input())
p=dict() #빈 딕셔너리 한개 만드는 거(딕셔너리는 키값 다)
def solution(n,p):
    for i in range(n):
        word=input()    #키값으로 word넣고
        p[word]=1   #value 값을 다 1로 만드는 거
    for i in range(n-1):    #실제 쓰인 단어들이 n-1개 들어옴
        word=input()
        p[word]=0           #입력받은 단어들이 있는 딕셔너리를 0으로 초기화(쓰인건 0으로 초기화함)
    for key, val in p.items():  #체크가 1되어 있는게 쓰이지 않은 단어. 그래서 출력하면 됨.
        #   for key, val in p.items(): 이렇게 하면 키값으로 동시 접근 가능
        if val==1:  #1이면 안 쓰인거니까 출력하면 됨.
            # print(key)
            return key;
            break

print(solution(n,p))
