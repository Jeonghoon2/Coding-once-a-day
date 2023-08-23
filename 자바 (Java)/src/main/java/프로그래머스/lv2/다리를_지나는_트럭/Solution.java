package 프로그래머스.lv2.다리를_지나는_트럭;

import java.util.Queue;
import java.util.LinkedList;

public class Solution {
    public static int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;

        Queue<Integer> bridge = new LinkedList<>();

        int i = 0;
        int outTruck = 0;

        while (outTruck != truck_weights.length){

            /* 다리에 있는 트럭 개수가 bridge_length 보다 적을 경우 */
            if (bridge.size() < bridge_length){

                /* 마지막 트럭일 경우 */
                if (i == truck_weights.length){
                    outTruck += 1;
                    answer += 1;
                    break;
                }else {
                    /* 다리에 있는 트럭과 들어오려는 트럭의 합산 무게가 weight 보다 작거나 같을 경우 */
                    if (bridge.stream().mapToInt(Integer::intValue).sum() + truck_weights[i] <= weight ){
                        bridge.add(truck_weights[i]);
                        i+=1;
                        answer +=1;
                    }
                    /* 무게를 초과할 경우*/
                    else {
                        bridge.poll();
                        outTruck+=1;
                        answer+=1;
                    }
                }

            }else {
                bridge.poll();
                outTruck+=1;
                answer+=1;
            }
        }


        return answer;
    }

    public static int solution2(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;

        Queue<Integer> q = new LinkedList<Integer>();

        for (int truck : truck_weights) {

            while (true){

                /* 다리에 아무것도 없을 경우 */
                if (q.isEmpty()){
                    q.offer(truck);
                    answer++;
                    break;
                }
                /* 다리에 허용 트럭 수가 꽉 찼을 경우 */
                else if (q.size() == bridge_length) {
                    q.poll();
                }
                /* 다리에 하나의 트럭이라도 있을 경우 */
                else {
                    /* 다음 트럭이 들어오려 할 때 무게가 초과하는 경우 */
                    if (q.stream().mapToInt(Integer::intValue).sum() + truck > weight){
                        q.offer(0);
                        answer++;
                    }
                    else {
                        q.offer(truck);
                        answer++;
                        break;
                    }
                }
            }
        }



        return answer + bridge_length;
    }

    public static void main(String[] args) {
        int bridge_length = 100;
        int weight = 100;
        int[] truck_weights = {10,10,10,10,10,10,10,10,10,10};

        System.out.println(solution2(bridge_length, weight,truck_weights));
    }
}
