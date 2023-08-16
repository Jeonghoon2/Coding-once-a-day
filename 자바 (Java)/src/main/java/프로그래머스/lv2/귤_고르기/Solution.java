package 프로그래머스.lv2.귤_고르기;


import java.util.*;

public class Solution {

    static HashMap<Integer, Integer> tangerines = new HashMap<>();

    public static int solution(int k, int[] tangerine) {
        int answer = 0;

        for (int i = 0; i< tangerine.length; i++) {
            tangerines.put(tangerine[i],tangerines.getOrDefault(tangerine[i],0) + 1);
        }

        List<Integer> ketList = new ArrayList<>(tangerines.keySet());
        Collections.sort(ketList, new customComparator());

        for (Integer e : ketList) {
            if (k <= 0)
                break;
            answer++;
            k -= tangerines.get(e);
        }
        return answer;
    }

    public static class customComparator implements Comparator<Integer>{

        @Override
        public int compare(Integer o1, Integer o2) {
            return tangerines.get(o2).compareTo(tangerines.get(o1));
        }
    }


    public static void main(String[] args) {
        int k = 6;
        int[] tangerine = {1, 3, 2, 5, 4, 5, 2, 3};
        System.out.println(solution(k,tangerine));
    }

}
