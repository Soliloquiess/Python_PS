word = input()

croatian_alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

# 크로아티아 알파벳을 다른 문자로 대체
for croatian in croatian_alphabets:
    word = word.replace(croatian, 'x')  # 크로아티아 알파벳을 'x'로 대체

# 크로아티아 알파벳을 제외한 나머지 알파벳의 개수 세기
croatian_count = word.count('x')
other_count = len(word) - croatian_count

print(croatian_count + other_count)


# a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# alpha = input()
# 
# for t in a:
#     alpha = alpha.replace(t, '*')
# 
# print(len(alpha))
# 
# #이거도 마찬가지 . a부분의 알파벳인 경우 *로 바꾸고 알파벳의 개수를 센다.
# 
# #a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
# #b = input()
# #for i in a:
# #    b = b.replace(i, 'a')
# #print(len(b))
# 
# 
