package String;

import java.util.Scanner;

import java.util.*;
class _11_문자열압축 {
    public String solution(String s){
        String answer="";
        s=s+" ";
        int cnt=1;
        for(int i=0; i<s.length()-1; i++){
            if(s.charAt(i)==s.charAt(i+1)) cnt++;
            else{
                answer+=s.charAt(i);
                if(cnt>1) answer+=String.valueOf(cnt);
                cnt=1;
            }
        }
        return answer;
    }

    public static void _11_문자열압축(String[] args){
        _11_문자열압축 T = new _11_문자열압축();
        Scanner sc = new Scanner(System.in);
        String str=sc.next();
        System.out.println(T.solution(str));
    }
}