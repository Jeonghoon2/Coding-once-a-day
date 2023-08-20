package 프로그래머스.lv2.프로세스;

import java.util.Collections;
import java.util.PriorityQueue;

public class Solution {

    /*
    * 1. 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.
    * 2. 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
    * 3. 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
    * 3-1. 한 번 실행한 프로세스는 다시 큐에 넣지 않고 그대로 종료됩니다.
    * */



    public static int solution(int[] priorities, int location) {

        int answer = 0;

        PriorityQueue<Integer> pQue = new PriorityQueue<>(Collections.reverseOrder());

        for (int i = 0; i < priorities.length; i++){
            pQue.offer(priorities[i]);
        }

        while (!pQue.isEmpty()){
            for (int i = 0; i < priorities.length; i++){
                if (priorities[i] == pQue.peek()){
                    if (i == location){
                        answer++;
                        return answer;
                    }
                    pQue.poll();
                    answer++;
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) {

        int[] priorities = {2, 1, 3, 2};

        int location = 2;

        System.out.println(solution(priorities, location));
    }


}
