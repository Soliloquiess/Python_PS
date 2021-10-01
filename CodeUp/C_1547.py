def f(n):
    index =0;
    for i in range(1,n+1):
        if((n%i)==0):
            index+=1;
    if(index==2):
        return True;
    else:
        return False;

n = int(input());
if(f(n)):
    print("prime");
else:
    print("composite");