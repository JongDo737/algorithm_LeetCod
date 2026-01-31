# 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다. 
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 
# 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

# bfs로 풀기
import sys
from collections import deque
input = sys.stdin.readline

def bfs(c):
    global count
    queue = deque()
    queue.append(c)

    visited[c] = True

    while queue:
        n = queue.popleft()
        for i in g[n]:
            if not visited[i]: # 방문하지 않았을 때
                queue.append(i)
                visited[i] = True
                count+=1

N = int(input())
M = int(input())

g = [[] for _ in range(N+1)]
for i in range(M):
    u,v = map(int, input().split())
    # 단방향
    g[u].append(v)
    g[v].append(u)

visited = [False] * (N+1)
count = 0

bfs(1)

print(count)