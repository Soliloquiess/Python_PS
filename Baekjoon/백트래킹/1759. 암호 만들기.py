L, C = map(int, input().split())
alpha = list(map(str, input().split()))
out = []
all_out = []
alpha.sort()

def solve(depth, idx, L, C):
    if depth == L:
        all_out.append(''.join(map(str, out)))
        return
    for i in range(idx, C):
        out.append(alpha[i])
        solve(depth+1, i+1, L, C)
        out.pop()

def password(list_check):
    for i in list_check:
        cons = 0
        vow = 0
        for j in i:
            if j in 'aeiou':
                cons += 1
            else:
                vow += 1
        if cons >= 1 and vow >= 2:
            print(i)
    return

solve(0, 0, L, C)
password(all_out)


#N과 M의 연장선에 있는 문제이다. C와 L로 이름만 바뀌었다.

# 조건은 최소 1개의 모음과 2개의 자음으로 구성된 암호이고,
#
# 사전식으로 가능성 있는 암호를 모두 출력하는 문제이다.
#
#
#
# 1. 먼저 얻은 배열을 sort() 한다. (문자열 순으로도 됨) L자리의 암호 얻기 위해서 DFS를 적용,
#
#     이 때 idx를 i+1을 넘겨주어 사전식으로 가능한 것들만 출력용 배열에 stack 한다.
#
# 2. 출력용 배열에서 1개 이상의 모음 / 2개 이상의 자음을 검사하여 print 한다.
#
#########


mo_list = ['a', 'e', 'i', 'o', 'u']

L, C = map(int, input().split())

# L 은 암호길이
# C 는 사용 문자 종류
alpha = list(input().split())
alpha.sort()


# 모음 갯수 , 자음 갯수
def make_pwd(mo, ja, pwd, pwd_len, last_idx):
    if mo >= 1 and ja >= 2 and len(pwd) == pwd_len:
        # 모음 개수 1 이상, 자음 개수 2이상, 암호문 길이가 L일 때
        print(pwd)
        return

    for c in range(last_idx + 1, len(alpha)):
        if alpha[c] in mo_list:
            make_pwd(mo + 1, ja, pwd + alpha[c], pwd_len, c)
        if alpha[c] not in mo_list:
            make_pwd(mo, ja + 1, pwd + alpha[c], pwd_len, c)


# 초기
for i in range(len(alpha)):
    if alpha[i] in mo_list:
        make_pwd(1, 0, alpha[i], L, i)
    else:
        make_pwd(0, 1, alpha[i], L, i)

#https://velog.io/@chuneeeee/%EB%B0%B1%EC%A4%80-1759-%ED%8C%8C%EC%9D%B4%EC%8D%AC