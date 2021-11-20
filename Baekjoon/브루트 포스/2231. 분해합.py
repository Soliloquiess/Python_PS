N = int(input()) #1
result = 0 #2
for i in range(1, N+1) :
    A = list(map(int, str(i))) #3
    result = i + sum(A) #4
    if result == N : #5
        print(i)
        break

    if i==N: #6
        print(0)
#https://yongku.tistory.com/entry/%EB%B0%B1%EC%A4%80-2231%EB%B2%88-%EB%B6%84%ED%95%B4%ED%95%A9-%ED%8C%8C%EC%9D%B4%EC%8D%ACPython