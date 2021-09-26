text = list(input());

for i in range(len(text)):
    if( ord('a')<= ord(text[i]) & ord(text[i])<ord('z')):
        print(chr(ord(text[i])-32), end = "");
    elif( ord('A')<= ord(text[i]) & ord(text[i])<ord('Z')):
        print(chr(ord(text[i])+32), end = "");
    else:
        print(text[i],end = "");


# string = input()
# print(string.swapcase())
