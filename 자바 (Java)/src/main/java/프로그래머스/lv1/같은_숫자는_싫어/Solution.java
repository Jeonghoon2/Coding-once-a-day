package 프로그래머스.lv1.같은_숫자는_싫어;

import java.util.ArrayList;

public class Solution {

    public static int[] solution(int []arr) {

        ArrayList<Integer> answer = new ArrayList<>();

        int cur_i = -1;

        for (int i = 0; i < arr.length; i++){

            if (!(cur_i == arr[i])){
                cur_i = arr[i];
                answer.add(arr[i]);
            }else {
                continue;
            }
        }
        return answer.stream().mapToInt(i->i).toArray();
    }

    public static void main(String[] args) {
        int[] arr = {1,1,3,3,0,1,1};
        System.out.println(solution(arr));
    }
}
