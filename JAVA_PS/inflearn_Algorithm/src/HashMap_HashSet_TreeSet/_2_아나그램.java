package HashMap_HashSet_TreeSet;

import java.util.HashMap;
import java.util.Scanner;

import java.util.*;
class _2_아나그램 {
    public String solution(String s1, String s2){
        String answer="YES";
        HashMap<Character, Integer> map=new HashMap<>();
        for(char x : s1.toCharArray()){
            map.put(x, map.getOrDefault(x, 0)+1);
        }
        for(char x : s2.toCharArray()){
            if(!map.containsKey(x) || map.get(x)==0) return "NO";	//x라는 키를 감소시키려 가져왔는데 없으면
            map.put(x, map.get(x)-1); //키가 있으니까 내려와서 map에 put해줌
        }
        return answer;
    }

    public static void main(String[] args){
        _2_아나그램 T = new _2_아나그램();
        Scanner sc = new Scanner(System.in);
        String a=sc.next();
        String b=sc.next();
        System.out.print(T.solution(a, b));
    }
}