from collections import deque
def solution(priorities, location):
    answer = 0
    queue = deque(priorities)
    
    # 두 리스트를 같이 정렬을 할 수 있는 방법
    value = priorities[location]
    
    priorities = sorted(priorities,reverse=True)
    # print(priorities)
    
    # index 값이랑 location 값이랑 같을 때, 우선순위가 낮다면 그때부터 + len(queue)
    index = 0
    while queue:
        
        temp = queue.popleft()
        
        # 더 큰 우선순위가 있을 때
        if priorities[0] > temp:
            
            queue.append(temp)
            print('False',location, index ,queue)
            if location == index:
                location += len(queue)
        elif priorities[0] <= temp: 
            print('True',location, index ,queue)
            del priorities[0]
            answer += 1
            if location == index:
                break
            
        index += 1
    
    return answer