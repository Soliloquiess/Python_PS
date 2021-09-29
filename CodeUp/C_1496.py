Arr=[]

n= int(input())
for i in range(n):
    Arr[i] = int(input());

for i in range(0,n-1,2):
    if(Arr[i]>Arr[i+1]):
        print(Arr[i+1]);
    else:
        print(Arr[i]);