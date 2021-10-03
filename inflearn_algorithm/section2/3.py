import sys
#sys.stdin=open("input.txt", "r")
n, k=map(int, input().split())
a=list(map(int, input().split()))
res=set() #res가 set이라는 자료구조가 되서 여러개의 자료를 넣어도 중복값이 있으면 제거한다. 여기서 set 쓰는 이유가 뭐지..
#set은 중복을 제거하는 자료구조
for i in range(n):
    for j in range(i+1, n): #j는 i뒤편부터 도는거 그리고 n전까지
        for m in range(j+1, n): #3번쨰 자료는 j뒤편부터 n까지
            res.add(a[i]+a[j]+a[m])
res=list(res)
res.sort(reverse=True) #큰 수 출력이니까 내림차순 정렬을 해야한다.
print(res[k-1]) #k번째는 인덱스-1에 있음.


# import sys
# #sys.stdin=open("input.txt", "r")
# n, k = map(int, input().split())
# a=list(map(int, input().split()))
# res=set() #res가 set이라는 자료구조가 되서 여러개의 자료를 넣어도 중복값이 있으면 제거한다. 여기서 set 쓰는 이유가 뭐지.. 아 결과값이라.
# #set은 중복을 제거하는 자료구조
#
# #야매
# a.sort();
# ans = a[n-1]+a[n-2]+a[n-5];
#
# print(ans);
# # res=list(res)
# # res.sort(reverse=True) #큰 수 출력이니까 내림차순 정렬을 해야한다.
# # print(res[k-1]) #k번째는 인덱스-1에 있음.