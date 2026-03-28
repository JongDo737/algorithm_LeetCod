import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;

        Map<Integer, Integer> gyul = new HashMap<>();
        
        for(int size :  tangerine) {
            gyul.put(size, gyul.getOrDefault(size, 0) + 1);
        }

        List<Integer> valList = gyul.values().stream().sorted().collect(Collectors.toList());
        
//         for(int val: valList) {
//             System.out.println(val);

//         }
        
        int index = valList.size() -1;
        // System.out.println("---");
        while(k >= 0) {
            // System.out.println(k);
            k -= valList.get(index);
            index -= 1;
            answer += 1;
            
            if(k<= 0) {
                break;
            }
        }
        
        return answer;
    }
}