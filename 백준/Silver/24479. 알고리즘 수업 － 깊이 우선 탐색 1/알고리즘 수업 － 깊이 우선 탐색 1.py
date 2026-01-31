import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(c): # 
    global order
    order += 1
    visited[c] = order

    for n in g[c]:
        if visited[n] == 0: # 방문하지 않았을 경우
            dfs(n)

N, M, R = map(int, input().split())

g = [[] for _ in range(N+1)]
for i in range(M):
    u,v = map(int, input().split())

    # 양방향
    g[u].append(v)
    g[v].append(u)

# 각 리스트 정렬
for i in range(N+1):
    g[i].sort()

# print(g)
visited = [0] * (N+1)
order = 0
dfs(R)

for i in range(1,N+1):
    print(visited[i])