from collections import deque
def solution(prices):
    answer = []
    
    prices_queue = deque(prices)
    
    last_price = []
    
    answer = [len(prices) - 1- i for i in range(len(prices))]
    
    # 지난 주식을 담는 last_price = (price, time)
    # prices_queue 반복문이 돌면서 (idx, price, -1) 로 초기화
    # -1 인 last_price 중에 값이 낮은 prices_queue 값이 들어오면 해당 값 제거, answer 추가
    
    index = 0
    while prices_queue:
        price = prices_queue.popleft()
        
        for i in range(len(last_price)-1,-1,-1):
            # last_price[i][0] = idx
            # last_price[i][1] = price
            # last_price[i][2] = -1
            
            # print(last_price[i], price, last_price[i][2] == len(prices)-1, last_price[i][1] > price)
            if last_price[i][1] > price:
                # print('여기:',last_price, price)
                answer[last_price[i][0]] = index - last_price[i][0]
                last_price.pop(i)
            
        
        last_price.append([index, price, len(prices)-1])
        index += 1
        
#         print(answer)
    
        
#     # 
#     print(answer)
    
    return answer