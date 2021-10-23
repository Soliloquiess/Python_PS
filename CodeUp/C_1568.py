def maxi(a,b ):
    index=a-1;
    ki = d[a-1];

    for i in range(a-1,b):
        if(d[i]>ki):
            index=i;
            ki=d[i];
    return index+1;

n= int(input())
d= list(map(int,input().split()));
a,b = list(map(int,input().split()));

print(maxi(a,b));