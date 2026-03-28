import java.util.*;
class Solution {
    public int[] solution(int n, String[] words) {
        int[] answer = new int[2];

        // Map으로 중복 검증
        Map<String,Boolean> map = new HashMap<>();
        map.put(words[0], true);
        
        char beforeC = words[0].charAt(words[0].length()-1);
        int count = 1;
        Boolean isClear = true;
        for(int i =1; i< words.length; i++) {
            count += 1;
            // 중복 검증
            if(map.containsKey(words[i])) {
                isClear = false;
                break;
            } else {
                map.put(words[i], true);
                
                // 끝말 성립
                if(beforeC != words[i].charAt(0)) {
                    // System.out.println(beforeC +":"+words[i].charAt(0));
                    isClear = false;
                    break;
                }
            }
            beforeC = words[i].charAt(words[i].length()-1);
            
        }
        // System.out.println(count);
        if(isClear) {
            answer[0] =0;
            answer[1] =0;
        }else {
            answer[0] = (count - 1) % n + 1; // 사람 번호
            answer[1] = (count - 1) / n + 1; // 차례
        }
        
        
        return answer;
    }
}