package inflearn_3_Twopointers_Slidingwindow;

import java.util.*;
class _4_연속부분수열 {	
	public int solution(int n, int m, int[] arr){
		int answer=0, sum=0, lt=0;
		for(int rt=0; rt<n; rt++){
			sum+=arr[rt];
			if(sum==m) answer++;	//확인해서 맞으면 answer값 증가
			while(sum>=m){
				sum-=arr[lt++];
				if(sum==m) answer++; 
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