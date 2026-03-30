import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
//        2
//        10 8 17
//        0 0
//        7 5
//        8 6
//        9 6
//        10 10 1
//        5 5

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int testCase = Integer.parseInt(br.readLine());
        for(int t=0; t<testCase; t++) {
            int answer = 0;
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int width = Integer.parseInt(st.nextToken());
            int height = Integer.parseInt(st.nextToken());
            int amount = Integer.parseInt(st.nextToken());

            int[][] visited = new int[height][width]; // 밭입니다. // true(방문전) false(방문)
            int x;
            int y;
            // 배추 표시
            List<List<Integer>> pointList = new ArrayList<>();
            for(int i=0; i<amount; i++) {
                List<Integer> forPointList = new ArrayList<>();
                st = new StringTokenizer(br.readLine(), " ");
                x = Integer.parseInt(st.nextToken());
                y = Integer.parseInt(st.nextToken());
                forPointList.add(x);
                forPointList.add(y);
                visited[y][x] = 1;
                pointList.add(forPointList);
            }
            // 반복문을 돌려서 배추가 있는 곳이면 dfs
            for(List<Integer> points: pointList) {
                if(visited[points.get(1)][points.get(0)] == 1) {
//                    System.out.println(points.get(0)+","+points.get(1));
                    visited = dfs(points.get(0),points.get(1), width, height, visited);
                    answer += 1;
                }
            }
            System.out.println(answer);
        }




    }
    public static int[][] dfs(int x, int y, int width, int height,  int[][] visited) {
        //  -> 동서남북 dfs
        visited[y][x] = 2; // 배추 있는데 방문


        // 서
        if(x > 0 && visited[y][x-1] == 1) {
            dfs(x-1,y,width,height,visited);
        }
        // 동
        if(x < width-1 && visited[y][x+1] == 1) {
            dfs(x+1, y, width,height,visited);
        }
        // 남
        if(y > 0 && visited[y-1][x] == 1) {
            dfs(x,y-1, width,height,visited);
        }
        // 북
        if(y < height-1 && visited[y+1][x] == 1) {
            dfs(x,y+1, width,height,visited);
        }

        return visited;
    }
}