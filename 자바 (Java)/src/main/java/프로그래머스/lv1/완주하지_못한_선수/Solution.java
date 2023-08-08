package 프로그래머스.lv1.완주하지_못한_선수;

import java.util.HashMap;
import java.util.Map;

public class Solution {

    public static String solution(String []participant, String []completion){

        HashMap<String,Integer> hash = new HashMap<String, Integer>();

        for (String p : participant) hash.put(p, hash.getOrDefault(p,0) + 1 );
        for (String c : completion) hash.put(c,hash.get(c)-1);

        return hash
                .entrySet()
                .stream()
                .filter(entry -> entry.getValue() != 0)
                .map(Map.Entry::getKey)
                .findFirst()
                .get();

    }

    public static void main(String []args){
        String[] participant = {"mislav", "stanko", "mislav", "ana"};
        String[] completion = {"stanko", "ana", "mislav"};

        System.out.println(solution(participant, completion));
    }
}
