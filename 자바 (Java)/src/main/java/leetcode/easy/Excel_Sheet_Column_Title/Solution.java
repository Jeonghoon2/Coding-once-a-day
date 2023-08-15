package leetcode.easy.Excel_Sheet_Column_Title;

import java.util.ArrayList;

public class Solution {
    public static String convertToTitle(int columnNumber) {

        StringBuilder columnName = new StringBuilder();

        while (columnNumber > 0) {
            // Find remainder
            int rem = columnNumber % 26;

            if (rem == 0) {
                columnName.append("Z");
                columnNumber = (columnNumber / 26) - 1;
            } else
            {
                columnName.append((char) ((rem - 1) + 'A'));
                columnNumber = columnNumber / 26;
            }
        }

        // Reverse the string and print result
        return String.valueOf(columnName.reverse());
    }

    public static void main(String[] args) {
        /*
        *
        * 1 -> A, 2 -> B ,,, Z -> 26, 27 -> AA
        *
        *
        *   701 / 26
        *
        * */

        int columnNumber = 52;

        System.out.println(convertToTitle(columnNumber));
    }
}
