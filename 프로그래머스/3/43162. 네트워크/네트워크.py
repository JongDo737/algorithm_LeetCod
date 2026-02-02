def solution(n, computers):
    answer = 0
    
    def dfs(c):
        # print(c)
        visited[c] = True
        for v in range(len(computers[c-1])):
            if computers[c-1][v] == 1 and not visited[v+1]: # 방문하지 않은 네트워크 시작점
                dfs(v+1)
            
    visited = [False] * (n+1)
    
    for i in range(n):
        # print(i+1,'번 노드 방문')
        if not visited[i+1]:
            # print('새 네트워크 발견')
            answer += 1
            dfs(i+1)
        
        
    # 방문하지 않은 개별 네트워크
    
    return answer