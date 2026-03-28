import java.util.*;
class Solution {
    public int solution(int[][] maps) {
        int answer = 0;

        // int[][] visited = new int[map[0].length][map.length];
        // [[1,0,1,1,1],
        //  [1,0,1,0,1],
        //  [1,0,1,1,1],
        //  [1,1,1,0,1],
        //  [0,0,0,0,1]]

        Boolean[][] visited = new Boolean[maps.length][maps[0].length];

        for(int y = 0; y < maps.length; y++) {
            for (int x = 0; x< maps[y].length; x++) {
                if(maps[y][x] == 1) {
                    visited[y][x] = false;
                }else {
                    visited[y][x] = true;
                }

            }
        }


        // 최단거리 = bfs

        return bfs(0,0, maps, visited);
    }
    public int bfs(int x, int y, int[][] maps, Boolean[][] visited) {
        Queue<int[]> queue = new LinkedList<>();
        int [] nowList = new int[3];
        nowList[0] = y;
        nowList[1] = x;
        nowList[2] = 1; // 움직인 칸 개수
        queue.add(nowList);
        visited[y][x] = true; // 방문

        while (!queue.isEmpty()) {
            int[] nowPoint = queue.poll();

            // System.out.print(nowPoint[0]+","+nowPoint[1]+" "+nowPoint[2]+"걸음" + "]-> [");

            // 목적지 도달
            if(nowPoint[0] == maps.length-1 && nowPoint[1] == maps[0].length-1) {
                // System.out.println("정답: "+nowPoint[2]);
                return nowPoint[2];
            }

            // [[1,0,1,1,1],
            //  [1,0,1,0,1],
            //  [1,0,1,1,1],
            //  [1,1,1,0,1],
            //  [0,0,0,0,1]]
            // 동쪽
//             System.out.println();
//             for(int y1 = 0; y1 < maps.length; y1++) {
//                 for (int x1 = 0; x1< maps[y1].length; x1++) {
//                     if(visited[y1][x1]){ // false는 미방문
//                         System.out.print(1);
//                     }else {
//                         System.out.print(0);
//                     }

//                 }
//                 System.out.println();
//             }

            // System.out.println((nowPoint[1] < maps[0].length-1  && !visited[nowPoint[0]][nowPoint[1]+1]));
            // System.out.println(nowPoint[1] > 0 && !visited[nowPoint[0]][nowPoint[1]-1]);
            // System.out.println(nowPoint[0] < maps.length-1 && !visited[nowPoint[0]+1][nowPoint[1]]);
            // System.out.println(nowPoint[0] > 0 && !visited[nowPoint[0]-1][nowPoint[1]]);

            int cy = nowPoint[0];
            int cx = nowPoint[1];
            int dist = nowPoint[2];

            if(cx < maps[0].length-1 && maps[cy][cx+1] == 1 && !visited[cy][cx+1]) {
                visited[cy][cx+1] = true;
                queue.offer(new int[]{cy, cx+1, dist+1});
            }

            // 서쪽
            if(cx > 0 && maps[cy][cx-1] == 1 && !visited[cy][cx-1]) {
                visited[cy][cx-1] = true;
                queue.offer(new int[]{cy, cx-1, dist+1});
            }

            // 남쪽
            if(cy < maps.length-1 && maps[cy+1][cx] == 1 && !visited[cy+1][cx]) {
                visited[cy+1][cx] = true;
                queue.offer(new int[]{cy+1, cx, dist+1});
            }

            // 북쪽
            if(cy > 0 && maps[cy-1][cx] == 1 && !visited[cy-1][cx]) {
                visited[cy-1][cx] = true;
                queue.offer(new int[]{cy-1, cx, dist+1});
            }

        }

        return -1;
    }
}