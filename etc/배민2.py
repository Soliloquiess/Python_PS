def solution(log):
    answer = ''
    int_list = list (log)

    list_a = []

    answer = []
    for i in range(0,len(log)):
        a= int(int_list[i][0:2]) *60;
        b= int(int_list[i][3:5])
        ans = a+b;
        list_a.append(ans);
    # print(list_a)
    odd = list_a[0::2];
    even = list_a[1::2];
    # print(odd);
    # print(even);
    for i in range(0, len(log)//2):

        answer.append(even[i]-odd[i]);
        if answer[i]<5:
            answer[i] =0;
        if answer[i]>105:
            answer[i] = 105;
    return answer

if __name__ == "__main__":
    print(solution(["08:30", "09:00", "14:00", "16:00", "16:01", "16:06", "16:07", "16:11"]))
    print(solution(["01:00", "08:00", "15:00", "15:04", "23:00", "23:59"]))

