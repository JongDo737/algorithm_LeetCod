from collections import deque

def solution(board):
    N = len(board)
    INF = float('inf')
    
    # dist[y][x][방향]: 0=상, 1=하, 2=좌, 3=우
    dist = [[[INF] * 4 for _ in range(N)] for _ in range(N)]
    
    # dy, dx, 방향인덱스
    directions = [(-1, 0, 0), (1, 0, 1), (0, -1, 2), (0, 1, 3)]
    
    queue = deque()
    
    # 시작점: 방향 미정이므로 4방향 모두 비용 0으로 시작
    for d in range(4):
        dist[0][0][d] = 0
        queue.append((0, 0, d, 0))
    
    while queue:
        y, x, direction, cost = queue.popleft()
        
        if dist[y][x][direction] < cost:
            continue
        
        for dy, dx, nd in directions:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N and board[ny][nx] == 0:
                # 방향이 같으면 직선(100), 다르면 코너 추가(500)
                add = 100 if nd == direction else 600
                new_cost = cost + add
                if dist[ny][nx][nd] > new_cost:
                    dist[ny][nx][nd] = new_cost
                    queue.append((ny, nx, nd, new_cost))
    
    print(dist[N-1][N-1])
    return min(dist[N-1][N-1])