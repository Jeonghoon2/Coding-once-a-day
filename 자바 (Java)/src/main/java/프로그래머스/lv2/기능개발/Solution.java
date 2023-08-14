package 프로그래머스.lv2.기능개발;


import java.util.*;

public class Solution {

    public static int[] solution(int[] progresses, int[] speeds) {

        List<Integer> list = new ArrayList<>();

        int[] works = new int[progresses.length];

        for (int i = 0; i <speeds.length; i++){
            works[i] = (100-progresses[i])/speeds[i];
            if ((100- progresses[i])% speeds[i] != 0){
                works[i] += 1;
            }
        }

        int x = works[0];
        int count = 1;


        for(int i = 1; i<progresses.length;i++){
            /* works[i]보다 x가 크다는 것은 works[i]가 x보다 일찍 끝나거다 동시에 끝난다는 말이다.  */
            if (x >= works[i]){
                count +=1;
            }else {
                list.add(count);
                count=1;
                x = works[i];
            }
        }

        list.add(count);

        int[] answer = new int[list.size()];

        for (int i = 0; i< list.size(); i++){
            answer[i] = list.get(i);
        }


        return answer;
    }

    public static void main(String[] args) {
        int[] progresses = {93, 30, 55};
        int[] speeds = {1, 30, 5};
        System.out.println(solution(progresses,speeds));
    }

}
