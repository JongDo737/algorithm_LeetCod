import java.util.Stack;
class Solution
{
    public int solution(String s)
    {
        int answer = 0;

        Stack<Character> stack = new Stack();

        for(char c : s.toCharArray()) {
            if(stack.size() == 0) {
                stack.push(c);
            }
            else {
                char temp = stack.pop();
                // 짝이 아닐 때
                if(temp != c) {
                    stack.push(temp);
                    stack.push(c);
                }
            }
        }

        if(stack.size() == 0) {
            answer = 1;
        }
        
        return answer;
    }
}