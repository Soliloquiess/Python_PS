def solution(record):
    answer = []
    userdict = {}
    # mes : record의 message
    # message를 받음과 동시에 유저 아이디 : 닉네임을 저장
    # Enter, Change가 들어온 경우 dictionary에 저장
    for mes in record:
        if (mes.split(' ')[0] == 'Enter') | (mes.split(' ')[0] == 'Change'):
            userdict[mes.split(' ')[1]] = mes.split(' ')[2]

    # for문을 돌면서, 하나씩 출력
    for mes in record:
        if mes.split(' ')[0] == 'Enter':
            # userdict[mes.split(' ')[1]] + '님이 들어왔습니다.' 이런식으로 해도 가능
            answer.append("{}님이 들어왔습니다.".format(userdict[mes.split(' ')[1]]))
        elif mes.split(' ')[0] == 'Leave':
            answer.append("{}님이 나갔습니다.".format(userdict[mes.split(' ')[1]]))
        else:
            pass
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]))

# idDict = dict()
#
#
# def solution(record):
#     answer = []
#     logList = []
#     for e in record:
#         dataList = e.split(" ")
#         if dataList[0] == "Leave":
#             logList.append([dataList[1], "님이 나갔습니다."])
#         elif dataList[0] == "Enter":
#             idDict[dataList[1]] = dataList[2]
#             logList.append([dataList[1], "님이 들어왔습니다."])
#         elif dataList[0] == "Change":
#             idDict[dataList[1]] = dataList[2]
#     print(logList)
#     for log in logList:
#         answer.append(idDict[log[0]] + log[1])
#     return answer
#https://kyome.tistory.com/108