package inflearn_6_Sort;


import java.util.*;
class _2_버블정렬 {	
	public int[] solution(int n, int[] arr){
		for(int i=0; i<n-1; i++){
			for(int j=0; j<n-i-1; j++){
				if(arr[j]>arr[j+1]){
					int tmp=arr[j];
					arr[j]=arr[j+1];
					arr[j+1]=tmp;
				}
			}	
		}
		return arr;
	}
	public static void main(String[] args){
		_2_버블정렬 T = new _2_버블정렬();
		Scanner kb = new Scanner(System.in);
		int n=kb.nextInt();
		int[] arr=new int[n];
		for(int i=0; i<n; i++) arr[i]=kb.nextInt();
		for(int x : T.solution(n, arr)) System.out.print(x+" ");
	}
}