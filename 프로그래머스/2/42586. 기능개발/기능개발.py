from collections import deque

def solution(progresses, speeds):
    answer = []
    # Queue로 구현
    # 하루에 (프로그래스 + speed)
    # 만약 앞 기능이 완성 안됐다면 continue
    
    queue = deque()
    queue_speads = deque()
    for i in range(len(progresses)):
        queue.append(progresses[i])
        queue_speads.append(speeds[i])
        
    
    # 하루 씩 계산
    while queue:
        # 하루 시작
        count = 0 # 하루 결과물
        for i in range(len(queue)):
            queue[i] = queue[i] + queue_speads[i]
        # 100% 이상인지 확인
        # print(queue)
        while queue:
            if queue[0] >= 100:
                queue.popleft()
                queue_speads.popleft()
                count+=1
                continue
            else:
                break # 앞 기능이 완성안됐다면 종료
        # 결과물 정산
        if count > 0: 
            answer.append(count)
    # print(answer)
    
    return answer