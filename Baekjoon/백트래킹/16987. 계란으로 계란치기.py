eggs = []
max_count = 0

def func(eggs,cur):
    global max_count
    if cur == len(eggs):
        count = 0
        for i in range(len(eggs)):
            if eggs[i][0] <= 0:
                count += 1
        if count > max_count:
            max_count = count
        return

    if eggs[cur][0] <= 0:
        func(eggs,cur+1)
    else:
        flag = False
        for i in range(len(eggs)):
            if i == cur or eggs[i][0] <= 0:
                continue
            eggs[cur][0] -= eggs[i][1]
            eggs[i][0] -= eggs[cur][1]
            flag = True
            func(eggs,cur+1)
            eggs[cur][0] += eggs[i][1]
            eggs[i][0] += eggs[cur][1]
        if not flag:
            func(eggs, cur+1)
    return



def main():
    global eggs
    N = int(input())
    while N:
        N -= 1
        tmp = list(map(int,input().split()))
        eggs.append(tmp)
    func(eggs,0)
    print(max_count)
    return



if __name__ == "__main__":
    main()

#   https://toy9910.tistory.com/m/20