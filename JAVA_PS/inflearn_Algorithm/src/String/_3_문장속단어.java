package String;

import java.util.*;
class _3_문장속단어 {
    public String solution(String str){
        String answer="";
        int m=Integer.MIN_VALUE;
        String[] s = str.split(" ");
        for(String x : s){
            int len=x.length();
            if(len>m){
                m=len;
                answer=x;
            }
        }
        return answer;
    }

    public static void main(String[] args){
        _3_문장속단어 T = new _3_문장속단어();
        Scanner sc= new Scanner(System.in);
        String str= sc.nextLine();
        System.out.print(T.solution(str));
    }
}




//import java.util.*;
//class _3_문장속단어 {
//    public String solution(String str){
//        String answer="";
//        int m=Integer.MIN_VALUE, pos;
//        while((pos=str.indexOf(' '))!=-1){
//            String tmp=str.substring(0, pos);
//            int len=tmp.length();
//            if(len>m){
//                m=len;
//                answer=tmp;
//            }
//            str=str.substring(pos+1);
//        }
//        if(str.length()>m) answer=str;
//        return answer;
//    }
//
//    public static void _3_문장속단어(String[] args){
//        _3_문장속단어 T = new _3_문장속단어();
//        Scanner sc = new Scanner(System.in);
//        String str= sc.nextLine();
//        System.out.print(T.solution(str));
//    }
//}