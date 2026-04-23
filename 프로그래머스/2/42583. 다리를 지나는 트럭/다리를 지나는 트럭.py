from collections import deque
def solution(bridge_length, weight, truck_weights):
    # 👉 “다리를 길이 bridge_length짜리 deque로 만들어라”
    answer = 0
    
    left_truck = deque(truck_weights)
    now = deque([0] * bridge_length)
    
    # print(now)
    now_score = 0
    while left_truck:
        answer += 1
        out_truck = now.popleft()
        if out_truck != 0:
            now_score -= out_truck
        
        if now_score + left_truck[0] <= weight:
            in_truck = left_truck.popleft()
            now_score += in_truck
            now.append(in_truck)
        
        else:
            now.append(0)
    
            
    return answer + bridge_length