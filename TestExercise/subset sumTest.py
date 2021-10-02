n = int(input());
arr = list(map(int, input().split()));

result=0;
max=0;
for j in range(1,n-1):

    result=arr[j-1]+arr[j]+arr[j+1];
    if(result>max):
        max = result;
        ans = j
    print(result);
    print(max);
    print(ans);

del arr[ans-1:ans+2];


result2=0
max2=0
for j in range(1,n-4):

    result2=arr[j-1]+arr[j]+arr[j+1];
    if(result2>max2):
        max2 = result2;
        ans2 = j
    print(result2);
    print(max2);
    print(ans2);

print(max+max2);