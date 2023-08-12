package Basic;

import java.util.Scanner;

class _아주기본적인자바입출력next_nextLine {
    public int solution(int n, String str){
        int answer = 0;

        String[] strArr= str.split(" ");
        int[] numArr= new int[n];
        for(int i = 0; i<n;i++) {
            numArr[i] = Integer.parseInt(strArr[i]);
        }
        answer += numArr[0];
        for(int i =1; i < n; i++) {
            if(numArr[i-1] < numArr[i]){
                answer += numArr[i];
            }
        }
        return answer;
    }

    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        _아주기본적인자바입출력next_nextLine T = new _아주기본적인자바입출력next_nextLine();
        int N = scanner.nextInt();
        scanner.nextLine();
        String str = scanner.nextLine();
        System.out.println(T.solution(N, str));
    }
}