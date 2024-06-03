
List =[];
max=0;
max_index=0;
for i in range(9):
    i = int(input())
    List.append(i)


for i in range(0,9):
    if(List[i] > max):
        max= List[i];
        max_index=i+1;
print(max,sep="");
print(max_index);