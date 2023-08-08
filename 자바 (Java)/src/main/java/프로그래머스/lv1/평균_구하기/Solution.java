package 프로그래머스.lv1.평균_구하기;

import org.apache.commons.lang3.time.StopWatch;

import java.util.Arrays;

class Solution {

    private static StopWatch st;



    public double solution(int[] arr) {

        double size = arr.length;
        return (Arrays.stream(arr).sum()) / size;
    }

    public double solution2(int[] arr) {

        double answer = 0;

        for (int i : arr) {
            answer += i;
        }

        return answer / arr.length;
    }

    public static void main(String[] args) {


        Solution sol = new Solution();
        int[] nums = {1,2,3,4};

        st =new StopWatch();
        st.start();

        System.out.println(" solution = " + sol.solution(nums));
        st.stop();

        System.out.println("st = " + st.getTime()*0.001);
    }
}
