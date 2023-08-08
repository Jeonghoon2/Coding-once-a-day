package 프로그래머스.lv1.나머지가_1이_되는_수_찾기;

import org.apache.commons.lang3.time.StopWatch;

import static java.util.stream.IntStream.range;



class Solution {

    /* 평균시간 0.0 */
    public int solution(int n) {
        int answer = 0;

        for (int i = 2; i<n; i++){
            if (n%i == 1){
                answer = i;
                break;
            }
        }
        return answer;
    }

    /* Stream 사용*/
    /* 평균 시간  0.017*/
    public int solution2(int n) {
        return range(2,n)
                .filter(i -> n %i == 1)
                .findFirst()
                .orElse(0);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();

        int n = 1000000000;

        StopWatch stopWatch = new StopWatch();

        stopWatch.start();

        System.out.println(sol.solution2(n));
        stopWatch.stop();

        System.out.println("stopWatch.getTime() = " + stopWatch.getTime()*0.001 + "ms");
    }

}