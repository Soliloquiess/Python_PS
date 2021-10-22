def solution(phone_number):
    a = list(phone_number)
    if(len(phone_number)>30 or len(phone_number)<1):
        return -1;
    if(a[0]=='0' and a[1]=='1' and a[2] =='0' and  a[3]=='-' and a[8]=='-' and len(phone_number)==13):
        return 1;
    if(a[0]=='0' and a[1]=='1' and a[2] =='0' and len(phone_number)==11):
        return 2;
    elif(a[0]=='+' and a[1]=='8' and a[2]=='2' and a[3] =='-' and a[4] =='1' and a[5] =='0' and a[6]=='-'and a[11]=='-' and len(phone_number)==16):
        return 3;
    else:
        return -1;

print(solution("010-1234-5678"))
print(solution("01012345678"))
print(solution("010-1212-333"))
print(solution("+82-10-3434-2323"))
print(solution("+82-010-3434-2323"))
print(solution("+82-010-3434-2323-12342314321592375021730"))
