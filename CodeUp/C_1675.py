text = list(input());

for i in range(len(text)):
    if( ord('d')<= ord(text[i]) & ord(text[i])<=ord('z')):
        print(chr(ord(text[i])-3), end = "");
    elif( text[i]== chr(ord('a'))):
        print("x", end = "");
    elif (text[i]== chr(ord('b'))):
        print("y", end = "");
    elif (text[i]== chr(ord('c'))):
        print("z", end = "");
    else:
        print(text[i], end = "")
