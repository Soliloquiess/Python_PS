def gcd(p, q):
    if(p==0):
        return q;
    return gcd(q%p,p);

def lcm(p,q):
    minN = p;
    maxN = q;
    if(minN>maxN):
        minN = q;
        maxN = p;
    return int(minN/gcd(maxN, minN) *maxN);


n, m = list(map(int,input().split()));
print(lcm(n,m));