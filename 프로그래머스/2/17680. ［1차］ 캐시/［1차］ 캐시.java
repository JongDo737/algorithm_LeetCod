import java.util.Deque;
import java.util.ArrayDeque;
class Solution {
    public int solution(int cacheSize, String[] cities) {
        int answer = 0;
        
        Deque<String> deque = new ArrayDeque<>();
        
        for(String city: cities) {
            // 캐시 적중
            city = city.toLowerCase();
            if(deque.contains(city)) {
                answer += 1;
                // LRU
                deque.remove(city);
                deque.add(city);
            } else {
                if(cacheSize > 0) {
                    if(deque.size() < cacheSize) {
                        deque.add(city);
                    
                    }else {
                        deque.poll();
                        deque.add(city);
                    }
                }
                answer += 5;
                    
            }
            
            // for(int i=0; i<deque.size(); i++) {
            //     System.out.print(deque.get(i)+" ");
            // }
            // System.out.println();
            
        }
        
        
        return answer;
    }
}