import java.util.Arrays;
class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        // 정렬 후 첫번째 마지막꺼 + 한다음 limit 초과 시 마지막꺼만 보내기

        Arrays.sort(people);
        
        // for(int a: Arrays.stream(people).toArray()) {
        //     System.out.println(a);
        // }
        
        int max_index = people.length-1;
        int min_index = 0;
        
        while (max_index >= min_index) {
            // System.out.println(people[min_index]+":"+people[max_index]);
            if(people[min_index] + people[max_index] <= limit) {
                
                // 같이 태우기
                min_index += 1;
                max_index -= 1;
                
                answer += 1;
            }else {
                max_index -= 1;
                answer += 1;
            }
        }
        
        return answer;
    }
}