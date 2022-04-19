package Stack_Queue;

import java.util.*;
class _3_크레인인형뽑기_카카오 {
    public int solution(int[][] board, int[] moves){
        int answer=0;
        Stack<Integer> stack = new Stack<>();
        for(int pos : moves){
            for(int i=0; i<board.length; i++){
                if(board[i][pos-1]!=0){
                    int tmp=board[i][pos-1];	//tmp에 인형번호 넣음
                    board[i][pos-1]=0;
                    if(!stack.isEmpty() && tmp==stack.peek()){	//비어있지 않으면서 스택 상단꺼를 꺼내옴.
                        answer+=2;
                        stack.pop();
                    }
                    else stack.push(tmp);
                    break;
                }
            }
        }
        return answer;
    }
    public static void main(String[] args){
        _3_크레인인형뽑기_카카오 T = new _3_크레인인형뽑기_카카오();
        Scanner kb = new Scanner(System.in);
        int n=kb.nextInt();
        int[][] board=new int[n][n];
        for(int i=0; i<n; i++){
            for(int j=0; j<n; j++){
                board[i][j]=kb.nextInt();
            }
        }
        int m=kb.nextInt();
        int[] moves=new int[m];
        for(int i=0; i<m; i++) moves[i]=kb.nextInt();
        System.out.println(T.solution(board, moves));
    }
}