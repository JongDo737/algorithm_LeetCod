import java.util.*;
class Solution {
    static int answer = 0;
    
    public int solution(int[] numbers, int target) {
        
        dfs(0,0, numbers, target);
        
        return answer;
    }
    void dfs(int index, int sum, int[]numbers, int target) {
        if (index == numbers.length) {
            // System.out.println(sum+":"+target);
            if (sum == target) {
                answer+= 1;
            }
            return ;
        }
        
        dfs(index+1, sum+numbers[index], numbers, target);
        dfs(index+1, sum-numbers[index], numbers, target);
    }
}