def solution(ledgers):
    month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # print(ledgers[0]);1 3 5 7 8 9 11
    month_sum = []
    for idx, value in enumerate(month):
        if idx == 0:
            month_sum.append(month[0])
        else:
            month_sum.append(month_sum[idx - 1] + month[idx])
    a=int(ledgers[0][0:2])
    b=int(ledgers[0][3:5])
    for i in range(len(ledgers)-1):
        print(int(ledgers[i+1][0:2]) - int(ledgers[i][0:2]))
    # if(a>1):
    #     month()
print(solution(["01/01 4 50000", "01/11 6 3555", "02/01 0 -23555", "02/25 5 5000", "03/25 0 -15000", "06/09 8 43951", "12/30 9 99999"]))

