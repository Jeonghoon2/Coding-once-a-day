package 프로그래머스.lv2.전화번호_목록;
import java.util.*;

public class Solution {

    public static boolean solution(String []phone_book){
        HashMap<String,Integer> book = new HashMap<String,Integer>();
        
        for (int i = 0; i < phone_book.length; i++){
            book.put(phone_book[i], i);
        }

        for (int i = 0; i < phone_book.length; i++){
            for (int j = 0; j < phone_book[i].length(); j++){
                if (book.containsKey(phone_book[i].substring(0,j))) return false;
            }
        }
        return true;
    }

    public static boolean solution2(String []phone_book){
        for(int i=0; i<phone_book.length-1; i++) {
            for(int j=i+1; j<phone_book.length; j++) {
                if(phone_book[i].startsWith(phone_book[j])) {return false;}
                if(phone_book[j].startsWith(phone_book[i])) {return false;}
            }
        }
        return true;
    }


    public static void main(String []args){
        String[] phoneBook = {"119", "97674223", "1195524421"};
        System.out.println(solution(phoneBook));
    }
}
