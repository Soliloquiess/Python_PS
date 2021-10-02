def swap(a,b):
    if(a>b):
        temp = a;
        a= b;
        b = temp
    print(a,b);
    # a,b = b,a;


    # return(a,b);

a,b = list(map(int,input().split()));
swap(a,b);
# print(swap(a,b));