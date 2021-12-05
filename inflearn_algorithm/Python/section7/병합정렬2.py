#병합정렬
def Dsort(lt,rt):
    if lt<rt:# 참아니면 바로 종료
        mid=(lt+rt)//2
        Dsort(lt,mid)
        Dsort(mid+1,rt)
        #본연의 일을 여기서 한다.

        p1=lt;
        p2=mid+1;
        tmp=[];
        while p1<=mid and p2<=rt:
            if arr[p1]<arr[p2]:
                tmp.append(arr[p1])
                p1+=1;
            else:
                tmp.append(arr[p2])
                p2+=1;
        if p1<=mid: tmp= tmp+arr[p1:mid+1]
        if p2<=rt: tmp=tmp+arr[p2];
        for i in range(len(tmp)):#0,1,2,3..이렇게 돈다.
            arr[lt+i] = tmp[i];
            #tmp에 넣어버리면 안됨. tmp는 그대로 증가하는데 arr에 lt+i해주는거.
            #i 가 처음



if __name__ == "__main__":
    arr=[23,11,45,36,15,67,33,21]
    print("Before sort:" ,end='');
    print(arr)
    Dsort(0,7)
    print();
    print("After sort: ", end=' ')
    print(arr)

#lt랑 rt더해서 2로 나눈 몫(중앙값)

#본연의 일? 0~7을 두 영역으로 나누고 새로운 리스트에 합침(앞에서 리스트 합치기 했었다)
#두 리스트 합치기(오름차순)했었다
#Dsort(0,7)은 다 끝마치면 본연의 일 한다.
#본연의 일 = 절반 절반 나누고 합치는 거.