import sys
from collections import deque
input = sys.stdin.readline

def bfs(c):
    queue = deque()
    queue.append(c)
    
    global order
    order += 1
    visited[c] = order

    while queue:
        n = queue.popleft()
        for i in g[n]:
            if visited[i] == 0: # 방문하지 않았다면
                queue.append(i)
                order+=1
                visited[i] = order


N, M, R = map(int, input().split())

g = [[] for _ in range(N+1)]

for i in range(1,M+1):
    u,v = map(int,input().split())

    g[u].append(v)
    g[v].append(u)

# 오름차순
for i in range(1,N+1):
    g[i].sort()

visited = [0] * (N+1)
order = 0

bfs(R)

for i in range(1,N+1):
    print(visited[i])