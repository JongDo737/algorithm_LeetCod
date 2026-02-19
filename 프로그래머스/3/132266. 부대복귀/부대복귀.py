from collections import deque
def solution(n, roads, sources, destination):
    answer = []
    path = [0] * n
    # 최단거리 BFS
    def bfs(c):
        visited[c] = True
        
        queue = deque()
        queue.append([c,0])
        # print('시작',c)
        while queue:
            # print('queue',queue)
            v, depth = queue.popleft()
            for i in g[v]:
                if not visited[i]:
                    # print('방문',i)
                    visited[i] = True
                    path[i-1] = depth+1
                    queue.append([i,depth+1])
                    
        # print(path)
        
        
    
    visited = [False] * (n+1)
    g = [[] for _ in range(n+1)]
    
    for u,v in roads:
        g[u].append(v)
        g[v].append(u)
    
    bfs(destination)
    
    for i in sources:
        if i == destination:
            answer.append(0)
        elif path[i-1] == 0:
            answer.append(-1)
        else:
            answer.append(path[i-1])
        
    
    return answer