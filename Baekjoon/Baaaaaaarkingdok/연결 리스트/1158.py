N, K = map(int, input().split())
arr = [i for i in range(1, N + 1)]  # 맨 처음에 원에 앉아있는 사람들(1차원 배열)

answer = []  # 제거된 사람들을 넣을 배열
num = 0  # 제거될 사람의 인덱스 번호

for t in range(N):
    num += K - 1
    if num >= len(arr):  # 한바퀴를 돌고 그다음으로 돌아올때를 대비해 값을 나머지로 바꿈
        num = num % len(arr)

    answer.append(str(arr.pop(num)))
print("<", ", ".join(answer)[:], ">", sep='')

#https://infinitt.tistory.com/213


# count, num = map(int, input().split())
#
# josephus = [i for i in range(1, count + 1)]
#
# result = []
# seqNo = num - 1
# while len(josephus):
#     if seqNo >= len(josephus):
#         # seqNo = seqNo - len(josephus)  얘두 댐!
#         seqNo = seqNo % len(josephus)
#     else:
#         result.append(str(josephus.pop(seqNo)))
#         seqNo += (num - 1)
#
# print("<", ", ".join(result), ">", sep='')


# list를 사용한다 해서 일자로, queue나 stack으로만 생각말고 일자인 선을 동그란 원형으로 만들었다 생각하면 이해하기 쉽다
# 반복해서 기억하기 위해 다시 말하면, pop()메서드는 항목을 추출해서 값을 가져오고 삭제한다. append()메서드는 제일 마지막 부분에 추가한다
# 요세푸쓰~~ 이름이 찰지네!
# 이상 끄으읕~