from collections import deque
def solution(m, n, puddles):
    answer = 0
    
    dp = [[0] *(m+1) for _ in range(n+1)]
    dp[0][2] = 1
    dp[2][0] = 1
    
    queue = deque(sorted(puddles, key=lambda x: (x[1], x[0])))
    water = [0,0]
    if queue:
        water = queue.popleft()
    for i in range(1,n+1):
        for j in range(1,m+1):
            # print(i,j)
            if water == [j,i]:
                if queue:
                    water = queue.popleft()
                else:
                    water = [0,0]
                continue
                # print('1111')
                
            dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
            # for row in dp:
            #     print(row)
            # print('----')
            
            
    # print(dp)
    
    
    
    return dp[n][m]