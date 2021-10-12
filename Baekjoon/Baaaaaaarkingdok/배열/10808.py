alpha = [0]*26
for i in input():   #이렇게 쓰면 입력한 문자 길이만큼 돈다.
    alpha[ord(i)-97]+=1
for i in alpha:
    print(i, end=' ')