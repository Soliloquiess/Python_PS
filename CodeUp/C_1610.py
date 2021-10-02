def mysubstr(word,start,count):
    for i in range(count):
        #끝이 개행문자x 띄어쓰기x (cde처럼 바로 뒤에 출력)
        print(word[start+i],end='')
w=input()
s,c=map(int,input().split())
mysubstr(w,s,c)