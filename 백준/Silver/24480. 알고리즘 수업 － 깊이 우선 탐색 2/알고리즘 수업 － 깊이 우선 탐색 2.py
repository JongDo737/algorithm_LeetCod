import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(c):
    global order
    order += 1
    visited[c] = order

    for n in g[c]:
        if visited[n] == 0:
            dfs(n)

N, M, R = map(int, input().split())

g = [[] for _ in range(N+1)]



for i in range(M):
    u,v = map(int, input().split())
    
    g[u].append(v)
    g[v].append(u)

for i in range(N+1):
    g[i] = sorted(g[i], reverse=True)

# print(g)


visited = [0] * (N+1)
order = 0

dfs(R)

for i in range(1,N+1):
    print(visited[i])