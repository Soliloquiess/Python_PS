def solution(board, moves):
    answer = 0
    moved=[0]  #인덱스 에러 방지
    for i in moves:
        i-=1
        for j in range(len(board)):
            if board[j][i] !=0:    #내려오면서 값이 없으면
                moved.append(board[j][i]) #moved리스트로 해당 값을 옮기고, 0으로 만듬
                board[j][i]=0
                if moved[-1] == moved[-2]:#만약 맨뒤의 요소 2개가 같으면
                    moved.pop(-1)     #뒤부터 2개를 pop
                    moved.pop(-1)
                    answer+=2 #인형이 2개 씩 없어지므로
                break  #크레인으로 인형을 하나 옮기면 다음 moves로 넘어가야함
    return answer

print(solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]],[1, 5, 3, 5, 1, 2, 1, 4]))