import java.util.Queue;
import java.util.LinkedList;

class Solution {
    public int solution(int n, int[][] computers) {
        int answer = 0;
        
        // BFS로 풀고 False인 부분 방문시켜서 answer += 1;
        
        int[] visited = new int[n];
        
        for(int i=0; i<n; i++) {    
            // 방문하지 않은 네트워크
            if (visited[i] == 0) {
                visited = bfs(i, visited, n, computers);
                answer += 1;
            }
            
        }
        return answer;
    }
    
    public int[] bfs(int c, int[] visited,int n, int[][] computers) {
        Queue<Integer> queue = new LinkedList();
        
        queue.add(c);
        
        while(!queue.isEmpty()) {
            int v = queue.poll();
            for(int i =0; i<n; i++) {
                if(i == c) continue; // 본인 노드
                
                if(computers[v][i] == 1 && visited[i] == 0) {
                    queue.add(i);
                    visited[i] = 1;
                }
            }
        }
        return visited;
        
        
    }
    
}