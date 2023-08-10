package 프로그래머스.lv2.연속_부분_수열_합의_개수;

import java.util.*;

public class Solution {

    public static int solution(int[] elements) {
        int answer = 0;

        /* Array의 특성인 fixed-size 때문에 수동의 배열을 늘려 줘야한다. */
        int[] newDouble = new int[elements.length*2];


        for(int i = 0; i < elements.length; i++){
            newDouble[i] = newDouble[i + elements.length] = elements[i];
        }

        HashSet<Integer> set = new HashSet<Integer>();

        for (int i = 1; i < elements.length+1; i++){
            for (int j = 0; j< elements.length; j++){
                set.add(Arrays.stream(newDouble,j,j+i).sum());
            }
        }

        answer = set.size();

        return answer;
    }

    public static void main(String[] args) {
        int[] elements = {7,9,1,1,4};

        System.out.println(solution(elements));
    }
}
