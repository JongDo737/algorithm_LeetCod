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
            if visited[i] == 0:
                queue.append(i)
                order +=1
                visited[i] = order

N, M, R = map(int, input().split())

g = [[] for _ in range(N+1)]

for i in range(M):
    u,v = map(int, input().split())

    g[u].append(v)
    g[v].append(u)

for i in range(1,N+1):
    g[i] = sorted(g[i], reverse=True)

# print(g)
visited = [0] * (N+1)
order = 0

bfs(R)

for i in range(1,N+1):
    print(visited[i])