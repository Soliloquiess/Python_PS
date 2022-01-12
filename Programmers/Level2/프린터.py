# def solution(priorities, location):
#     answer = 0
#     while True:
#         max_num = max(priorities) # 리스트에서 가장 큰수를 구한다.
#         for i in range(len(priorities)): # 리스트를 처음부터 확인한다
#             if max_num == priorities[i]: # 만약 가장 큰 수와 리스트의 요소와 일치하면
#                 answer += 1 # 프린트한 것으로 간주하고 answer에 1 추가
#                 priorities[i] = 0 # 프린트한 요소는 0으로 표시
#                 max_num = max(priorities) # 가장 큰 수를 다시 구한다.
#                 if i == location: # 만약 location과 i가 일치하면 answer을 반환한다.
#                     return answer

def solution(priorities, location):
    loc = [i for i in range(len(priorities))]
    final_loc = []

    while len(priorities) != 0:
        if priorities[0] == max(priorities): # 최고 우선순위일 때, 프린트
            final_loc.append(loc.pop(0))
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))

    return final_loc.index(location) + 1




# def solution(priorities, location):
#     count=0
#     while(len(priorities)!=0):
#         if location==0: #출력 여부를 확인되는 맨 앞순서로 왔을 경우
#             if priorities[0]<max(priorities): #더 중요도가 큰 문서가 있으면
#                 priorities.append(priorities.pop(0)) #맨뒤로 보냄
#                 location=len(priorities)-1 #location을 맨끝으로 설정(배열길이-1)
#             else: ##더 우선순위가 높은 것이 없다면 내꺼가 출력되는 것이므로 return으로 끝냄
#                 return count+1
#         else:
#             if priorities[0]<max(priorities):
#                 priorities.append(priorities.pop(0))
#                 location-=1 #맨앞 요소가 뒤로 갔기 때문에 location이 1 줄어듦
#             else:
#                 priorities.pop(0) #맨앞요소 출력됨
#                 location-=1 #맨앞 요소가 출력됐기 때문에 location이 1 줄어듦
#                 count+=1 #(출력번째수 +1)





# print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))