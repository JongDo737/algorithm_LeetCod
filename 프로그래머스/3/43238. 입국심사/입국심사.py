def solution(n, times):
    answer = 0
    
    left = 0
    mid = 0
    right = times[-1] * n
    
    def count_n(time):
        count = 0
        for i in times:
            # print(times, i, time)
            count += time // i
        return count
    # index = 10
    while left <= right:
        mid = (left + right) // 2
        if count_n(mid) >= n:
            answer = mid  # 일단 후보로 등록
            right = mid - 1 # 더 작은 시간이 있는지 보러 가기
        else:
            left = mid + 1 # 시간이 더 필요함
    
    return answer