import sys
#sys.stdin=open("input.txt", "r")
s=input()
res=0
for x in s:
    if x.isdecimal(): # isdecimal은 isdigit과 같은데 안전하게 변환하려면 이거 쓰래.(문자열 들어온거 숫자로 바꿔주는 함수)
        #https://soooprmx.com/archives/10159

        res=res*10+int(x)   #숫자 있으면 10 곱해서 한칸 좌측이동 시켜주는거고 x가 숫자값 들어온거(찾은거)니까 x를 더해주면 됨.
print(res)


cnt=0   #cnt=0는 약수 구하기 위한 개수 초기화 해준거.
for i in range(1, res+1):   #res까지 돌면서
    if res%i==0:            #i로 나눴을때 0이 되면 그 i값이 약수값이고
        cnt+=1              #약수 찾는게 아니라 약수 값 찾으라 했으니까 cnt 출력하면 개수 출력하는거.
print(cnt)
