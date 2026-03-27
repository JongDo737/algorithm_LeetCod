import java.util.*;
class Solution {
    public String solution(String s) {
        String answer = "";
        
        String[] list = s.split(" ");
        int[] intList = new int[list.length];
        
        for(int i =0; i< list.length; i++) {
            intList[i] = Integer.parseInt(list[i]);
        }
        
        Arrays.sort(intList);
        
        return intList[0] + " " + intList[intList.length - 1];
    }
}