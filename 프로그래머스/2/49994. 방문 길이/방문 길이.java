import java.util.*;
class Solution {
    public int solution(String dirs) {
        int answer = 0;
        // visited 체크하면 되나 ?
        // boolean[][] visited = new boolean[10][10];
        
        Set<String> visitedMap = new HashSet<>();
        
        
        // answer += 1;
        // (5,5) 시작
        int x = 5;
        int y = 5;
        for(char dir: dirs.toCharArray()) {
            int nx = x;
            int ny = y;
            
            
            if (y < 10 && dir == 'U') {
                ny ++;
            }else if (x > 0 && dir == 'L') {
                nx --;
            }else if (x < 10 && dir == 'R') {
                nx ++;
            }else if (y > 0 && dir == 'D') {
                ny --;
            }
            
            if (x == nx && y == ny) continue;
            
            visitedMap.add(x+""+y+">"+nx+""+ny);
            visitedMap.add(nx+""+ny+">"+x+""+y);
            
            x = nx;
            y = ny;
            // System.out.println(visitedMap);
        }
        
        answer = visitedMap.size() / 2;
        
        
        return answer;
    }
}