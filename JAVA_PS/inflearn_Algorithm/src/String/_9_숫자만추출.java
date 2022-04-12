package String;

import java.util.Scanner;

import java.util.*;
class _9_숫자만추출 {
    public int solution(String s){
        int answer=0;
//		String answer="";
        for(char x : s.toCharArray()){
            if(x>=48 && x<=57) answer = answer*10 +(x-48);
			/*if(Character.isDigit(x)){
				answer=answer*10+ Character.getNumericValue(x);
			}*/
//			if(Character.isDigit(x)) answer+=x;
        }
        return answer;
//		return Integer.parseInt(answer);
    }

    public static void _9_숫자만추출(String[] args){
        _9_숫자만추출 T = new _9_숫자만추출();
        Scanner sc = new Scanner(System.in);
        String str=sc.next();
        System.out.print(T.solution(str));
    }
}