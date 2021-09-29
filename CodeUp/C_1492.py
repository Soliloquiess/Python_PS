
num = int(input());
sum =0;

Arr = list(map(int,input().split()));


for i in range(num):

    # Arr.append(int(input()));
    sum +=Arr[i];
    Arr[i]=sum;



for j in range(num):
    print(Arr[j],end=" ");