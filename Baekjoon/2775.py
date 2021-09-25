T=  int(input());

apt =[[0 for i in range(19)]for j in range(19)]

for i in range(15):
    apt[i][1]= 1;
    apt[0][i] =i;


for i in range( 1,15):
    for j in range(2,15):
        apt[i][j] = apt[i][j-1]+ apt[i-1][j];



for i in range(T):
    k=int(input());
    n=int(input());
    print(apt[k][n]);