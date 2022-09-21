#수(num)와 배열을 입력받아 차례대로 num개의 요소만 포함된 새로운 배열을 리턴해야 합니다
def take(num, arr):
    if(num==1 or len(arr)==1 ):
        return [arr[0]];
    return [arr[0]]+take(num-1,arr[1:]);

print(take(2,[2,7,11,15]));

