package String;

import com.sun.tools.javac.Main;

import java.util.*;
class _2_대소문자_변환 {
    public String solution(String str){
        String answer="";
        for(char x : str.toCharArray()){
            if(Character.isLowerCase(x)) {  //소문자면
                answer+=Character.toUpperCase(x);   //대문자로
            }
            else answer+=Character.toLowerCase(x);  //반대로 대문자면 소문자로

        }
        return answer;
    }

    public static void main(String[] args){
        _2_대소문자_변환 T = new _2_대소문자_변환();
        Scanner sc = new Scanner(System.in);
        String str=sc.next();
        System.out.print(T.solution(str));
    }
}

