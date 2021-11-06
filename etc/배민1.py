def solution(arr):
    answer = []
    max=-10
    min = 1000000;
    index1=0;
    index2=0;
    index3=0;

    for i in range(0, len(arr)):
        if (arr[i] == 1):
            index1+=1;
        if (arr[i] == 2):
            index2 += 1;
        if (arr[i] == 3):
            index3 += 1;

    if(index1==index2==index3):
        answer.append(0)
        answer.append(0)
        answer.append(0)

        return answer
    if(index1>index2):
        if(index1>index3):
            max = index1;
        elif(index3>index1):
            max = index3;

    elif(index2>index1):
        if(index2>index3):
            max = index2;
        else:
            max = index3;
    elif(index3>index1):
        if(index3>index2):
            max= index3;
        else:
            max = index2;
    ans1 = max - index1
    ans2 = max - index2
    ans3 = max - index3

    answer.append(ans1);
    answer.append(ans2);
    answer.append(ans3);
    # answer.append(index1)
    # answer.append(index2)
    # answer.append(index3)

    return answer


if __name__ == "__main__":
    print(solution([2, 1, 3, 1, 2, 1]))
    print(solution([3, 3, 3, 3, 3, 3]))
    print(solution([1, 2, 3]))
