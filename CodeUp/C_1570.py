
num=int(input())

def lower_bound(k):
    for i in range(0,num+1):
        if(k<=d[i]):
            return i+1;
            break;
    return n;

d = list(map(int, input().split()));
k = int(input());
print(lower_bound(k));

