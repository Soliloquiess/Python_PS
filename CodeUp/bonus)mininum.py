#최소값 구하기

arr = [5,3,7,9,2,5,2,6];
#arrMin=float('inf');


min=float('inf'); #float 형의 최대값을 넣어줄 수 있따.

#min=float('-inf'); #이렇게 하면 float 형의 최소값을 넣어줄 수 있따.

arrMin = arr[0];
for i in range(len(arr)):
    if arr[i] < arrMin:
        arrMin = arr[i];
print(arrMin);

for x in arr:
    if x<arrMin:
        arrMin =x;
print(arrMin);