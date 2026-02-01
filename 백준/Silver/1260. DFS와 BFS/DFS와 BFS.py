# 첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다. 
# 다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 
# 입력으로 주어지는 간선은 양방향이다.

import sys
from collections import deque
input = sys.stdin.readline

def dfs(c):
    visited_dfs[c] = True
    answer_dfs.append(c)

    for v in g[c]:
        if not visited_dfs[v]: # 방문하지 않았다면
            # print(v, visited_dfs)
            visited_dfs[v] = True
            dfs(v)

def bfs(c):
    queue = deque()
    queue.append(c)

    visited_bfs[c] = True
    answer_bfs.append(c)

    while queue:
        v = queue.popleft()
        for i in g[v]:
            if not visited_bfs[i]: # 방문하지 않았다면
                queue.append(i)
                visited_bfs[i] = True
                answer_bfs.append(i)



N, M, V = map(int, input().split())

g = [[] for _ in range(N+1)]

for i in range(M):
    u,v = map(int, input().split())

    g[u].append(v)
    g[v].append(u)

for i in range(1,N+1):
    g[i].sort()

visited_dfs = [False] * (N+1)
visited_bfs = [False] * (N+1)

answer_dfs = []
answer_bfs = []

dfs(V)
bfs(V)

print(' '.join(map(str, answer_dfs)))   # 한 줄씩 출력
print(' '.join(map(str, answer_bfs)))