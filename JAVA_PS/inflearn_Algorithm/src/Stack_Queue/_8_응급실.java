package Stack_Queue;

import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

import java.util.*;
import java.io.*;

class Person{
    int id;
    int priority;
    public Person(int id, int priority){
        this.id=id;
        this.priority=priority;
    }
}

class _8_응급실 {
    public int solution(int n, int m, int[] arr){
        int answer=0;
        Queue<Person> Q=new LinkedList<>();
        for(int i=0; i<n; i++){
            Q.offer(new Person(i, arr[i]));	//객체 생성해서 큐에다 넣음
        }
        while(!Q.isEmpty()){
            Person tmp=Q.poll();
            for(Person x : Q){	//tmp라는 환자가 진료 받을수 있는지 알기 위해 이렇게 돈다.
                if(x.priority>tmp.priority){
                    Q.offer(tmp);
                    tmp=null;
                    break;
                }
            }
            if(tmp!=null){	//널이 아니면 위가 참이 아니라는 소리
                answer++;
                if(tmp.id==m) return answer;	//tmp의 대기번호가 m이 맞으면 바로 리턴
            }
        }
        return answer;
    }

    public static void main(String[] args) throws IOException {
        _8_응급실 T = new _8_응급실();
        Scanner kb = new Scanner(System.in);
        int n=kb.nextInt();
        int m=kb.nextInt();
        int[] arr = new int[n];
        for(int i=0; i<n; i++){
            arr[i]=kb.nextInt();
        }
        System.out.println(T.solution(n, m, arr));
    }
}