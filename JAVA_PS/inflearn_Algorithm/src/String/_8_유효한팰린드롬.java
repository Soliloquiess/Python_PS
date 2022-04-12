package String;

import java.util.Scanner;

import java.util.*;
class _8_유효한팰린드롬 {
    public String solution(String s){
        String answer="NO";
        s=s.toUpperCase().replaceAll("[^A-Z]", "");	//A~Z까지 문자 아니면 공백까지 포함 다 제거
        String tmp=new StringBuilder(s).reverse().toString();
        if(s.equals(tmp)) answer="YES";
        return answer;
    }

    public static void _8_유효한팰린드롬(String[] args){
        _8_유효한팰린드롬 T = new _8_유효한팰린드롬();
        Scanner sc = new Scanner(System.in);
        String str=sc.nextLine();
        System.out.print(T.solution(str));
    }
}