import java.util.Stack;
class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
        // 바로 뒤에있는 수가 자신 보다 클경우
        Stack<Integer> stack = new Stack<>();
        
        for(int i=0; i<numbers.length; i++) {
            answer[i] = -1;
            
            if(stack.isEmpty()) {
                stack.push(i);
                continue;
            }
            
            // 뒷 큰수 찾았다면
            while(!stack.isEmpty()) {
                if(numbers[stack.peek()] < numbers[i]) {
                    answer[stack.pop()] = numbers[i];
                }else {
                    break;
                }
            }
            stack.push(i);
            
        }
        
        
        return answer;
    }
}