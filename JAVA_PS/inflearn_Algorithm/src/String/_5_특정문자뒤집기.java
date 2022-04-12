package String;

import java.util.*;
class _05_특정문자뒤집기 {
    public String solution(String str){
        String answer;
        char[] s=str.toCharArray();
        int lt=0, rt=str.length()-1;
        while(lt<rt){
            if(!Character.isAlphabetic(s[lt])) lt++;    //알파벳이 아니면 lt 증가(오른쪽 이동)
            else if(!Character.isAlphabetic(s[rt])) rt--;   //알파벳이 아니면 rt감소(왼쪽 이동)
            else{
                char tmp=s[lt];
                s[lt]=s[rt];
                s[rt]=tmp;
                lt++;
                rt--;
            }
        }
        answer=String.valueOf(s);
        return answer;
    }

    public static void _05_특정문자뒤집기(String[] args){
        _05_특정문자뒤집기 T = new _05_특정문자뒤집기();
        Scanner sc = new Scanner(System.in);
        String str=sc.next();
        System.out.println(T.solution(str));
    }
}


//
//---------
//
//
//        import java.util.*;
//class _05_특정문자뒤집기 {
//    public String solution(String str){
//        String answer;
//        char[] s=str.toCharArray();
//        int lt=0, rt=str.length()-1;
//        while(lt<rt){
//            if(!(s[lt] >= 97 && s[lt] <= 122) && !(s[lt] >= 65 && s[lt] <= 90)) lt++;
//            else if(!(s[rt] >= 97 && s[rt] <= 122) && !(s[rt] >= 65 && s[rt] <= 90)) rt--;
//            else{
//                char tmp=s[lt];
//                s[lt]=s[rt];
//                s[rt]=tmp;
//                lt++;
//                rt--;
//            }
//        }
//        answer=String.valueOf(s);
//        return answer;
//    }
//
//    public static void _05_특정문자뒤집기(String[] args){
//        _05_특정문자뒤집기 T = new _05_특정문자뒤집기();
//        Scanner sc = new Scanner(System.in);
//        String str=sc.next();
//        System.out.println(T.solution(str));
//    }
//}