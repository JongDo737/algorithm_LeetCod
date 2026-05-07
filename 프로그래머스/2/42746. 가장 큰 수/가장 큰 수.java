import java.util.*;
class Solution {
    public String solution(int[] numbers) {
        String answer = "";
        
        List<Integer> numString = new ArrayList<>();
        for(int i=0; i< numbers.length; i++) {
            numString.add(numbers[i]);
        }
        // System.out.println(numString);
        Collections.sort(numString, (a,b) -> {
            String as = String.valueOf(a);
            String bs = String.valueOf(b);
            
            return -Integer.compare(Integer.parseInt(as+bs),Integer.parseInt(bs+as));
        });
        // System.out.println(numString);
        
        StringBuilder sb = new StringBuilder();
        for(int i=0; i<numString.size(); i++) {
            sb.append(numString.get(i));
        }
        
        if (sb.charAt(0) == '0') {
            return "0";
        }

        
        return sb.toString();
    }
}