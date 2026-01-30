from collections import deque
def solution(queue1, queue2):
    answer = -2
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    # sum 함수를 매번 사용하지 않고 변수를 만들어 +-로 연산처리하는게 좋을 듯
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    
    count = len(queue1) + len(queue2) +2
    
    # print(queue1, sum1)
    # print(queue2, sum2)
    
    # 원소는 정수이므로 두 큐의 합이 홀수이면 어떻게 해도 각 큐의 합을 정수로 같게 만들 수 없음(ex. 17 -> 8.5)
    if (sum(queue1) + sum(queue2)) % 2 == 1:
        return -1
    
    while sum1 != sum2:
        if not queue1 or not queue2:
            return -1
        if count > 0:
            if queue1 and queue2 and sum1 < sum2:
                temp = queue2.popleft()
                queue1.append(temp)
                answer+=1
                sum1 += temp
                sum2 -= temp
                count -= 1
            elif queue1 and queue2 and sum1 > sum2:
                temp = queue1.popleft()
                queue2.append(temp)
                answer+=1
                sum1 -= temp
                sum2 += temp
                count -= 1
        else:
            return -1
    return answer +2