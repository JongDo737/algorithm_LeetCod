import java.util.*;
class Solution {
    public int solution(int n) {
        int answer = 0;
        System.out.println();
        List<Integer> list = new ArrayList<>();
        
        list.add((int)n/2);
        list.add((int)n/2 +1);
        
        int max = (int) n/2 + 1;
        int min = (int) n/2;
        
        // 15
        int now = max + min;
        
        while (min >= 1) {
            // System.out.println("now: "+now);
            // System.out.println("max: "+max);
            // System.out.println("min: "+min);
            if (now == n) {
                answer += 1;
                now = now - max;
                max = max -1;
            }
            // 합계가 n보다 크면
            else if (now > n) {
                now = now - max;
                max = max -1;
            }
            // 합계가 n 보다 작을떄
            else if (now < n) {
                min = min -1;
                now = now + min;
            }
            
        }
        
        return answer+1;
    }
}