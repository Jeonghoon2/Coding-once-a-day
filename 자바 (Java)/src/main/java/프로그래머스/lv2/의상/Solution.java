package 프로그래머스.lv2.의상;
import java.util.*;

public class Solution {

    public static int solution(String[][] clothes) {
        int answer = 1;
        HashMap<String,Integer> hashMap = new HashMap<String,Integer>();
        
        for (int i = 0; i < clothes.length; i++){
            for (int j = 0; j<clothes[i].length-1; j++){
               hashMap.put(clothes[i][1], hashMap.getOrDefault(clothes[i][1],1) + 1);
            }
        }

        for (String key : hashMap.keySet()){
            answer *= hashMap.get(key);
        }
        
        return answer-1;
    }

    public static void main(String []args){
        String[][] clothes = {
                {"yellow_hat", "headgear"},
                {"blue_sunglasses", "eyewear"},
                {"green_turban", "headgear"}
        };

        System.out.println(solution(clothes));


    }
}
