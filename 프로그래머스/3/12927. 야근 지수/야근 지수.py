import heapq
def solution(n, works):
    answer = 0
    
#     # 효율성 실패
#     if not works:
#         return 0
    
#     for i in range(n):
#         works.sort(reverse=True)
        
#         if works[0] == 0:
#             return 0
#         n -= 1
#         works[0] = works[0] - 1
#     for i in works:
#         answer += i * i

    # heap을 사용하자 Max Heap
    heap = []
    
    for i in works:
        heapq.heappush(heap, -i)
        
    for i in range(n):
        max_value = -heapq.heappop(heap) # max니까 음수로
        
        if max_value == 0:
            return 0
        
        max_value -= 1
        heapq.heappush(heap, -max_value)
    
    # print(heap)

    for i in heap:
        answer += i*i
        # print(answer)
    
    return answer