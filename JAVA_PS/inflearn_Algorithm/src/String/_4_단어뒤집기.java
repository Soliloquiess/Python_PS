package String;

//import java.util.*;
//class _04_단어뒤집기 {
//    public ArrayList<String> solution(String[] str){
//        ArrayList<String> answer=new ArrayList<>();
//        for(String x : str){
//            String tmp=new StringBuilder(x).reverse().toString();
//            answer.add(tmp);
//        }
//        return answer;
//    }
//
//    public static void _04_단어뒤집기(String[] args){
//        _04_단어뒤집기 T = new _04_단어뒤집기();
//        Scanner sc = new Scanner(System.in);
//        int n=sc.nextInt();
//        String[] str=new String[n];
//        for(int i=0; i<n; i++){
//            str[i]=sc.next();
//        }
//        for(String x : T.solution(str)){
//            System.out.println(x);
//        }
//    }
//}




import java.util.*;
class _04_단어뒤집기 {
    public ArrayList<String> solution(int n, String[] str){
        ArrayList<String> answer=new ArrayList<>();
        for(String x : str){
            char[] s=x.toCharArray();
            int lt=0, rt=x.length()-1;
            while(lt<rt){
                char tmp=s[lt];
                s[lt]=s[rt];
                s[rt]=tmp;
                lt++;
                rt--;
            }
            String tmp=String.valueOf(s);
            answer.add(tmp);
        }
        return answer;
    }

    public static void main(String[] args){
        _04_단어뒤집기 T = new _04_단어뒤집기();
        Scanner sc = new Scanner(System.in);
        int n=sc.nextInt();
        String[] str=new String[n];
        for(int i=0; i<n; i++){
            str[i]=sc.next();
        }
        for(String x : T.solution(n, str)){
            System.out.println(x);
        }
    }
}
