def DFS(v):
    if v > 7:
        return
    else:
        print(v, end=' ')#프린터를 앞에 하면 전위순회
        DFS(v * 2)
        #print(v, end=' ')  # 프린터를 중간에 하면 중위순회(왼쪽 먼저 처리)
        DFS(v * 2 + 1)
        #print(v, end=' ')  # 프린터를 마지막에 하면 중위순회


if __name__ == "__main__":
    DFS(1)