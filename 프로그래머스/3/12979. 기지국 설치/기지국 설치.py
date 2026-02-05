def solution(n, stations, w):
    answer = 0
    
    min_num = 0
    max_num = 0
    start = 1
    for station in stations:
        
        min_num = station-w
        max_num = station+w
        
        if min_num < 0:
            min_num = 0
        if max_num > n:
            max_num = n
        
        # print(min_num, start, min_num-start)
        if start < min_num:
            answer += int((min_num-start) / (w+w+1))
            if (min_num-start) % (w+w+1) != 0:
                answer += 1
        start = max_num+1
        # print(answer)
    
    # print('마무리', start,n,n-start+1)
    if start <= n:
        answer += int((n-start+1) / (w+w+1))
        if (n-start+1) % (w+w+1) != 0:
            answer += 1
    
    return answer