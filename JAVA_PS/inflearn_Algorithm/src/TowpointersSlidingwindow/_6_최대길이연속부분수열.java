package TowpointersSlidingwindow;

import java.util.Scanner;

import java.util.*;
class _6_최대길이연속부분수열 {
    public int solution(int n, int k, int[] arr){
        int answer=0, cnt=0, lt=0;
        for(int rt=0; rt<n; rt++){
            if(arr[rt]==0) cnt++;
            while(cnt>k){   //cnt는 k주어진 개수( 만약 2를 넘어가면 맨 왼쪽에 있는 걸 뺴고 lt를 오른쪽으로 한칸 이동시켜준다.
                //
                if(arr[lt]==0) cnt--;
                lt++;
            }
            answer=Math.max(answer, rt-lt+1);
        }
        return answer;
    }

    public static void main(String[] args){
        _6_최대길이연속부분수열 T = new _6_최대길이연속부분수열();
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        int k=sc.nextInt();
        int[] arr=new int[n];
        for(int i=0; i<n; i++){
            arr[i]=sc.nextInt();
        }
        System.out.print(T.solution(n, k, arr));
    }
}