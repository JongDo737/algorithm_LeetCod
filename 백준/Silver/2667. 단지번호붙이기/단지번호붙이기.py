import sys
# from collections import queue
input = sys.stdin.readline

def house(cx,cy):
    global index
    while cx < N:
        # print('(',cx,cy,')')
        
        
        if g[cx][cy] == 1 and not visited[cx][cy]: # 1인데 방문하지 않았을 때
            # print('외부',cx,cy,index)
            house_type.append(0)
            house_cnt.append(0)

            dfs(cx,cy,index)
            index += 1
        cy += 1

        if cy == N:
            cy = 0
            cx += 1
        

def dfs(cx, cy, index):
    
    if cy == N or cx == N:
        return 0

    if g[cx][cy] == 1 and not visited[cx][cy]:
        house_cnt[index] += 1

        visited[cx][cy] = True
        # print('내부',index,cx,cy, house_cnt[index])
        
        if cx > 0:
            dfs(cx-1,cy, index) # 좌
        if cy > 0:
            dfs(cx,cy-1, index) # 위
        dfs(cx+1,cy,index) # 우
        dfs(cx,cy+1, index) # 아래
    else:
        return 0

N = int(input())
g = [[] for _ in range(N)]

for i in range(N):
    temp = input().split('\n')[0]
    g[i] = [int(i) for i in temp]

visited = [[False] * N for _ in range(N)]

house_type = []
house_cnt = []
index = 0

house(0,0)

house_cnt.sort()

print(len(house_type))
for i in house_cnt:
    print(i)