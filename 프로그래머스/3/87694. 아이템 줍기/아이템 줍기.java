import java.util.Queue;
import java.util.LinkedList;
class Solution {
    public int solution(int[][] rectangle, int characterX, int characterY, int itemX, int itemY) {
        int answer = 0;
        
        // 최단거리 BFS
        // [[1,1,7,4], 1
        //  [3,2,5,5], 2
        //  [4,3,6,9], 3 5
        //  [2,6,8,8]] 4 6
        
        int[][] available = new int[101][101];
        int[][] visited = new int[101][101];
        
        for(int[] r: rectangle) {
            int x1 = r[0] * 2;
            int y1 = r[1] * 2;
            int x2 = r[2] * 2;
            int y2 = r[3] * 2;
            
            for(int i=x1; i<=x2; i++) {
                for(int j=y1; j<=y2; j++) {
                    
                    // 사각형 내부
                    if (i > x1 && i < x2 && j > y1 && j < y2) {
                        available[i][j] = 2;
                    }
                    else if (available[i][j] != 2) {
                        available[i][j] = 1;
                    }
                }
            }
        }
        
        // 가능한 곳 그리기
        answer = bfs(available, visited, characterX*2, characterY*2, itemX*2 ,itemY*2);
        
        
        return answer;
    }
    int bfs(int[][] available,int[][] visited, int cX, int cY, int itemX, int itemY) {
        // 좌표를 담은 Queue
        Queue<int[]> queue = new LinkedList<>();
        int sum = 0;
        queue.add(new int[]{cX, cY, sum});
        visited[cX][cY] = 1;
        
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            
            cX = cur[0];
            cY = cur[1];
            sum = cur[2];
            // System.out.println(cX+":"+cY+" = "+sum);
            
            if (cX == itemX && cY == itemY) {
                return sum / 2;
            }
            
            // 동
            if (cX+1 < 101 && available[cX+1][cY] == 1 && visited[cX+1][cY] == 0) {
                queue.add(new int[]{cX+1, cY, sum+1});
                visited[cX+1][cY] = 1;
            }
            // 서
            if (cX-1 >= 0 && available[cX-1][cY] == 1 && visited[cX-1][cY] == 0) {
                queue.add(new int[]{cX-1, cY, sum+1});
                visited[cX-1][cY] = 1;
            }
            // 남
            if (cY-1 >= 0 && available[cX][cY-1] == 1 && visited[cX][cY-1]  == 0) {
                queue.add(new int[]{cX, cY-1, sum+1});
                visited[cX][cY-1] = 1;
            }
            // 북
            if (cY+1 < 101 && available[cX][cY+1] == 1 && visited[cX][cY+1] == 0) {
                queue.add(new int[]{cX, cY+1, sum+1});
                visited[cX][cY+1] = 1;
            }
        }
        return 0;
        
    }
}