class Solution {
    public String solution(String s) {
        // String answer = "";
        
        StringBuilder string = new StringBuilder();
        
        s = s.toLowerCase();
        
        boolean isFirst = true;
        
        for (char c : s.toCharArray()) {
            if(c == ' ') {
                string.append(c);
                isFirst = true;
            }else {
                if(isFirst) {
                    string.append(Character.toUpperCase(c));
                    isFirst = false;
                }else{
                    string.append(c);
                }
            }
        }
        
        
        return string.toString();
    }
}