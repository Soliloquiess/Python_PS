N= int(input());

arr = [];
sum =0;

arr = list(map(int, input().split()))


arr.sort();
M= arr[N-1]

for i in range(N):
    arr[i] = (arr[i]/M) *100
    sum += arr[i];

ans = sum / N;
print(ans)
