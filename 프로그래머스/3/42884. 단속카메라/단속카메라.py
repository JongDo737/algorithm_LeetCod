from collections import deque
def solution(routes):
    answer = 0
    routes.sort(key=lambda x: (x[0], x[1]))
    
    queue = deque(routes)
    in_road = [] # [차번호i, 들어온 곳]
    index = 0
    while queue:
        start,end = queue.popleft()
        # print(in_road, start,end)
        if in_road and in_road[0] < start: # 차량이 먼저 나가야할 때
            # print('지금:',in_road[0], start)
            in_road = []
            answer += 1
            
        
        in_road.append(end)
        in_road.sort()
    
    if in_road:
        answer += 1
    return answer