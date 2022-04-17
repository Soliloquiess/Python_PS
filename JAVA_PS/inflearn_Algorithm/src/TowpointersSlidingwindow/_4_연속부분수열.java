package TowpointersSlidingwindow;

import java.util.Scanner;

import java.util.*;
class _4_연속부분수열 {
    public int solution(int n, int m, int[] arr){
        int answer=0, sum=0, lt=0;
        for(int rt=0; rt<n; rt++){
            sum+=arr[rt];
            if(sum==m) answer++;
            while(sum>=m){
                sum-=arr[lt++]; // lt 위치 뺴고 lt 증가
                if(sum==m) answer++;    //lt 빼고 나서도 일치 하는지 확인. lt 뺴고도 m이 아니면 rt부분 증가시키는 거.
            }
        }
        return answer;
    }

    public static void main(String[] args){
        _4_연속부분수열 T = new _4_연속부분수열();
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int m=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0; i<n; i++){
            arr[i]=sc.nextInt();
        }
        System.out.print(T.solution(n, m, arr));
    }
}