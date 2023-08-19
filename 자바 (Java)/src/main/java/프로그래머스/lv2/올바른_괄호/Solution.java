package 프로그래머스.lv2.올바른_괄호;

import javax.xml.stream.FactoryConfigurationError;
import java.util.ArrayList;
import java.util.List;
import java.util.Stack;

public class Solution {

    /**
    * 효율성 테스트 실패
     * */
    public static boolean solution(String s){

        boolean answer = true;

        Stack<String> st = new Stack<>();


        for (int i = 0; i < s.length(); i++){

            String cur_i = s.substring(i, i + 1);

            if (st.size() == 0){
                if (cur_i.equals(")")){
                    return false;
                }
                st.add(cur_i);
            }else {
                if (cur_i.equals(")")){
                    if (st.contains("(")){
                        st.pop();
                    }else {
                        return false;
                    }
                }else {
                    st.add(cur_i);
                }
            }
        }

        if (st.size() >= 1){
            return false;
        }

        return answer;
    }

    /* 효율성 태스트 실패 */
    public static boolean solution2(String s){
        boolean answer = true;

        Stack<String> st = new Stack<>();

        for (int i = 0; i < s.length(); i++){

            String cur_i = s.substring(i, i+1);

            if (cur_i.equals(")") && st.empty()){
                return false;
            } else if (cur_i.equals(")") && st.contains("(")) {
                st.pop();
            }else {
                if (cur_i.equals("(")){
                    st.add("(");
                }
            }

            }

        if (st.size() >=1 ){
            return false;
        }
        return answer;

    }

    /* 효율성 태스트 실패 */
    public static boolean solution3(String s){
        boolean answer = true;

        Stack<String> st = new Stack<>();

        for (int i = 0; i < s.length(); i++){
            if (s.charAt(i) == '('){
                st.push("(");
            }else if (s.charAt(i) == ')'){
                if (st.isEmpty()){
                    return false;
                }
                st.pop();
            }
        }
        return st.isEmpty();
    }



    public static void main(String[] args) {

        String s = "(()(";

        System.out.println(solution3(s));

    }
}
