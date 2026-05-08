class Solution {
    public int solution(String s) {
        int answer = 1; // 팰린드롬의 최소 길이는 무조건 1
        
        // pivot을 0부터 문자열 끝까지 이동시킵니다.
        for (int pivot = 0; pivot < s.length(); pivot++) {
            
            // 1. 홀수 길이 팰린드롬 (pivot이 정중앙)
            int left = pivot;
            int right = pivot;
            // 배열 범위를 벗어나지 않고, 양끝 글자가 같을 때만 확장(size++)
            while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
                int currentLen = right - left + 1;
                answer = Math.max(answer, currentLen);
                left--;  // 왼쪽으로 한 칸 확장
                right++; // 오른쪽으로 한 칸 확장
            }
            
            // 2. 짝수 길이 팰린드롬 (pivot과 pivot+1 사이가 중앙)
            left = pivot;
            right = pivot + 1;
            while (left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
                int currentLen = right - left + 1;
                answer = Math.max(answer, currentLen);
                left--;
                right++;
            }
        }
        
        return answer;
    }
}