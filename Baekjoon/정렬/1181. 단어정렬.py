# 1181번 : 단어 정렬
n = int(input())

word = []
for i in range(n):
    word.append(input())

set_word = list(set(word))  #중복 제거

sort_word = []
for i in set_word:  #리스트 들어있는 단어들 묶어줌.
    sort_word.append((len(i), i))

#
# """
#
# print해본 결과:
#
# [(2, 'im'), (4, 'wait'), (4, 'more'), (5, 'yours'), (3, 'but'), (4, 'wont'), (6, 'cannot'), (1,
#
# 'i'), (2, 'no'), (2, 'it'), (8, 'hesitate')]
#
# """

# 위에 출력된 것처럼 이제 sorted 코드를 쓰면, 앞에 있는 숫자와 뒤에 있는 문자가 순서대로 자동 정렬이 됩니다.


# 마지막으로 sorted로 정렬한 리스트의 인덱싱 하나마다 2개의 인수(argument)가 있기 때문에
#
# for문에서 len(word)와 word 2개의 매개변수(parameter)를 쓴 후
#
# 최종 출력 값에 필요한 word만 출력하면 풀이 끄--읏

result = sorted(sort_word)

for len_word, word in result:
    print(word)

# https://wook-2124.tistory.com/468