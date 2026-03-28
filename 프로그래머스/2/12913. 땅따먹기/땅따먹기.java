import java.util.Arrays;
class Solution {
    int solution(int[][] land) {
        int answer = 0;

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        // System.out.println("Hello Java");
        
        // dp
        int[][] dp = new int[land.length][land[0].length];
        
        int beforeYul = -1;
        
        // 열 먼저
        for(int i =0; i<land.length; i++) { 
            for(int j =0; j<land[0].length; j++) {
                // 첫번째 열
                if(i == 0) {
                    dp[i][j] = land[0][j];
                    
                }else {
                    // 밟고온 점수와 합산
                    int point = 0;
                    for(int k =0; k<land[0].length; k++) {
                        // 검증 (같은 열 불가)
                        if (j != k) {
                            point = dp[i-1][k] + land[i][j];
                            
                        }
                        if (dp[i][j] < point) {
                            dp[i][j] = point;
                        }
                        // for(int q=0; q< dp.length; q ++) {
                        //     for(int w=0; w<dp[0].length; w++) {
                        //         System.out.print(dp[q][w]+" ");
                        //     }
                        //     System.out.println();
                        // }
                        // System.out.println("-----");
                    } // for k
                } // if 첫 행 구분
                
            } // for j
        } // for i
        int[] result = dp[land.length-1]; // 마지막 행
        
        Arrays.sort(result); // 마지막행 정렬
        
        return result[result.length -1]; // 가장 큰 값 반환
    }
}