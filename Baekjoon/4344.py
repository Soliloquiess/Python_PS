N=10001;
def fn (N):
    result = N;
    while(N!=0):
        result += N%10;
        N = N/10;
    return result;

arr = []
for i in range(1, 10001):
    arr[i] = 1;


for i in range(1,10001):
    index = fn(i);
    if(index <= N):
        arr[index]=0;

for i in range(N):
    if(arr[i] !=0
    ):
        print(i);