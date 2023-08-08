package 프로그래머스.lv1.포켓몬;

import java.util.*;

public class Solution {

    public static int solution1(int []nums){
        int answer = 0;

        int N = nums.length/2;
        nums = Arrays.stream(nums).distinct().toArray();
        answer = Math.min(nums.length, N);
        return answer;
    }

    public static int solution2(int []nums){
        HashSet<Integer> hash = new HashSet<>();

        for (int i = 0; i<nums.length; i++){
            hash.add(nums[i]);
        }

        if (hash.size() > nums.length / 2) return nums.length/2;

        return hash.size();
    }

    public static void main(String []args){
        int[] arr = {3,1,2,3};

        System.out.println(solution1(arr));

    }

}
