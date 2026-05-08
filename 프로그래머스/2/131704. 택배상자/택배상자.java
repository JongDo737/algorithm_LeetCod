import java.util.Deque;
import java.util.ArrayDeque;
class Solution {
    public int solution(int[] order) {
        int answer = 0;
        
        // Deque로 구현
        // 기사가 원하는 박스 번호 = order[orderIdx]
        // 원하는 박스 번호가 아닐 때, push(i+1)
        // 원하는 박스번호가 나오면 while문으로 orderIdx 늘려가면서 조회
        
        Deque<Integer> belt = new ArrayDeque<>();
        
        int orderIdx = 0;
        for(int i=0; i<order.length; i++) {
            belt.push(i+1);
            
            // 순서가 맞을 때
            while (!belt.isEmpty() && order[orderIdx] == belt.peek()) {
                    answer ++;
                    orderIdx ++;
                    belt.pop();
        
            }
            
            
            
        }
        
        return answer;
    }
}