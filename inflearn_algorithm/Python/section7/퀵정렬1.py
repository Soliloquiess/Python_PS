#병합정렬
def Qsort(lt,rt):
    if lt<rt:# 피벗설정 피벗은 맨앞이든 맨뒤든 랜덤이든 설정에 따라 달라디직도 한다
        #여기서는 피벗을 맨뒤에 설저
        mid=(lt+rt)//2
        Qsort(lt,mid)
        Qsort(mid+1,rt)
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
    arr=[45,21,23,36,15,67,11,60,20,33]
    print("Before sort:" ,end='');
    print(arr)
    Qsort(0,9)
    print();
    print("After sort: ", end=' ')
    print(arr)

#피벗 생성해서 파티션 나눈다. 피벗보다 높으면 오른쪽 작으면 왼쪽
#맨 처음 피벗 쓰고
#Qsort(lt,pos-1),
#Qsort(pos+1, rt)로 만든다.