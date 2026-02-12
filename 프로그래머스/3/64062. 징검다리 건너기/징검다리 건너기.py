def solution(stones, k):
    answer = 0
    
    # k만큼의 start와 start+k 에서 가장 max값이 작은 곳을 찾으면 될듯 -> 시간초과

    def can_cross(stones, k, mid):
        cant_cross = 0
        
        for stone in stones:
            temp = stone - mid
            if temp < 0:
                cant_cross+=1
                if cant_cross >= k:
                    return False
            else:
                cant_cross = 0
        return True
            
    # 인원수 이진탐색
    left = 0
    right = max(stones)
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_cross(stones, k, mid):
            answer = mid
            left = mid + 1
        else: 
            right = mid - 1
    
    
    return answer