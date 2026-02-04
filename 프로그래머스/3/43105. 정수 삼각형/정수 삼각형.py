def solution(triangle):
    answer = []
    if len(triangle) == 1:
        return triangle[0][0]
    
    # triangle = triangle[:3][:]
    # print(triangle)
    dp = [[0] * len(triangle) for _ in range(len(triangle))]
    
    dp[0][0] = triangle[0][0]
    dp[1][0] = dp[0][0] + triangle[1][0]
    dp[1][1] = dp[0][0] + triangle[1][1]
    
    # print(dp)
    for i in range(2,len(triangle)):
        for j in range(i+1):
            # print(i,j)
            
            # 제일 왼쪽이면
            if j == 0:
                dp[i][j] = triangle[i][j] + dp[i-1][j]
                continue
            
            # 끝이면 
            if j == i:
                dp[i][j] = triangle[i][j] +  dp[i-1][j-1]
                continue
                
            # 중간이면
            value = dp[i-1][j-1]
            # for row in dp:
            #     print(row)
            # print('여기',dp[i-1][j-1],dp[i-1][j])
            if value < dp[i-1][j]:
                value = dp[i-1][j]
            
            dp[i][j] = triangle[i][j] + value
            
            
#     print('----')
            
#     for row in dp:
#         print(row)
    
    # print()
    # print(answer)
    return sorted(dp[-1][:])[-1]