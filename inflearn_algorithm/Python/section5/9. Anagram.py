import sys
#sys.stdin=open("input.txt", "r")
# a=input()
# b=input()
# str1=dict()
# str2=dict()
# def solution(a,b):
#     for x in a:     #a라는 문자열 하나하나가 x에 대응됨
#         str1[x]=str1.get(x, 0)+1    #x라는 키값(알파벳). x라는 알파벳이 있냐 없으면 0을, 있으면 그 키값의 밸류값을 리턴해서 +1 해주는거 (카운팅)
#     for x in b:
#         str2[x]=str2.get(x, 0)+1 #두개 문자열 입력받으니까 바로 위랑 똑같이 하면 된다.
#
#     for i in str1.keys():   #str1이라는 딕셔너리의 키값만 담음(확인해 보는 작업)
#         if i in str2.keys():    #str1에 존재하는 키값이 str2의 딕셔너리에 존재하는 키값에도 존재하는지 봐야한다.
#             #str1이라는 딕셔너리에 있는 키값은 str2라는 딕셔너리 키값들 중 있어야 한다. 그래야만 아나그램이다.
#             #str1에있는 키가 str2라는 딕셔너리에도 있는지 봐야한다.
#             #키가 일치하면(str1에 있는 키가 str2에도 있다고 확인되면 그 대문자의 개수와 그 첫번째 문자열의 대문자의 개수
#
#             if str1[i]!=str2[i]:
#                 #str1[i] 이건 첫번째 문자열의 대문자 개수
#                 #str2[i] 두번쨰 문자열의 대문자 개수
#                 #이게 참이면 아나그램 아니므로 no
#                 # print("NO")
#                 return "NO"
#                 break
#         else:   #if i in str2.keys()이 존재하지 않으면(key가 존재 안하니까)
#             #그럼 아나그램 아니므로 no
#             # print("NO")
#             return "NO"
#             break
#     else:      #문자열이 완벽하게 다 맞으면 정상포문 끝나므로 yes 출력.
#         # print("YES")
#         return "YES"
# print(solution(a,b));


# 딕셔너리 쓰면 아주 편하게 사용가능
# 딕셔너리는 리스트와 달리 숫자 말고 문자,알파벳, 단어도 인넥스로 사용 가능하다. 리스트는 정수로만 인덱스 쓰지만
# 딕셔너리는 문자 알파벳으로 키값을 쓸 수 있다. 이 단어들을 1로 ㄹ체크하고 쓰인 단어가 들어오면 그 값을 0으로 바꾸면
# 1로 남은게 쓰이지 않은 단어.
# 이 방법이 더 좋긴 하다.
#<개선된 코드>(위에서 비교하는게 복잡해서 바꿈)
import sys
#sys.stdin=open("in1.txt", "r")
a=input()
b=input()
sH=dict()
def solution(a,b):
    for x in a:     #여기서 카운팅 한 것들을
        sH[x]=sH.get(x, 0)+1

    for x in b:     #여기서 원 상태로 복구하는거.(빼줘서)
        sH[x]=sH.get(x, 0)-1
    #a,b가 아나그램이면 문자의 순서만 다를 뿐 성분은 똑같음.
    #a에서 돌면서 1씩 증가시키고 b에서 다시 -1 하면 원상복구됨. 그럼 그 키값의 밸류는 0이 됨.

    for x in a:
        if(sH.get(x)>0): #0이 아닌게 발견 되면 아나그램이 아님.
            # print("NO")
            return "NO";
            break;
    else:               #다 0이면 아나그램임
        # print("YES")
        return "YES"
print(solution(a,b));