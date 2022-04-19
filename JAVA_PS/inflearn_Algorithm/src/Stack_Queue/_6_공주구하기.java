package Stack_Queue;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

import java.util.*;
class _6_공주구하기 {
    public int solution(int n, int k){
        int answer=0;
        Queue<Integer> Q=new LinkedList<>();
        for(int i=1; i<=n; i++) {
            Q.offer(i);
        }
        while(!Q.isEmpty()){
            for(int i=1; i<k; i++) {
                Q.offer(Q.poll());  //k번쨰가 아니면 맨 앞에 요소를 맨뒤에 넣는다(offer)
            }
            Q.poll();
            if(Q.size()==1) {
                answer=Q.poll();
            }
        }
        return answer;
    }
    public static void main(String[] args){
        _6_공주구하기 T = new _6_공주구하기();
        Scanner kb = new Scanner(System.in);
        int n=kb.nextInt();
        int k=kb.nextInt();
        System.out.println(T.solution(n, k));
    }
}