package Stack_Queue;

import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

import java.util.*;

class _7_교육과정설계 {
    public String solution(String need, String plan){
        String answer="YES";
        Queue<Character> Q=new LinkedList<>();
        for(char x : need.toCharArray()) {
            Q.offer(x);
        }
        for(char x : plan.toCharArray()){
            if(Q.contains(x)){  //Q가 X에 있는지 확인
                if(x!=Q.poll()) {   //x돌면서 큐에서 뽑은게 x와 같지 않으면(순서 확인 하는거)
                    return "NO";
                }
            }
        }
        if(!Q.isEmpty()) return "NO";
        return answer;
    }
    public static void main(String[] args){
        _7_교육과정설계 T = new _7_교육과정설계();
        Scanner kb = new Scanner(System.in);
        String a=kb.next();
        String b=kb.next();
        System.out.println(T.solution(a, b));
    }
}