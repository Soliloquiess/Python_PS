#병합정렬
def Qsort(lt,rt): #lt=0,rt=9
    if lt<rt:# 피벗설정 피벗은 맨앞이든 맨뒤든 랜덤이든 설정에 따라 달라디직도 한다
        #여기서는 피벗을 맨뒤에 설저
        pos = lt;
        pivot = arr[rt]
        for i in range(lt,rt):
            if arr[i] <=pivot: # pivot값보다 작으면 스왑이 일어난다.
                arr[i], arr[pos]=arr[pos],arr[i];
                pos+=1;
        arr[rt], arr[pos] = arr[pos], arr[rt];
        # return
        Qsort(lt, pos-1)
        Qsort(pos+1, rt)

        #퀵소트는 파티션작업하고 계속 분할해서 1개까지 들어가면 끝남(정렬 끝)
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