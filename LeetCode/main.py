def take(num, arr):
    if(num==1 or len(arr)==1 ):
        return [arr[0]];
    return [arr[0]]+take(num-1,arr[1:]);

print(take(2,[2,7,11,15]));

