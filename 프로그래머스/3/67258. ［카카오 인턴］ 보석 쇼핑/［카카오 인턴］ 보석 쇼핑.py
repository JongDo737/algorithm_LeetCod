def solution(gems):
    answer = [0,1000000]
    
    check = {}
    check_set = set(gems)
    start = 0
    end = 0
    # 이중포문으로 쓴 맛 보고 이중 포인트로 변경
    # while 
    for i in range(len(gems)):
        # print('1end:',end,check)
        check[gems[end]] = check.get(gems[end],0) + 1
        # print('2end:',end,check)
        while len(check) == len(check_set):
            # print(check, start, end)
            
            if end-start < answer[1] - answer[0]:
                answer = [start+1, end+1]
            
            check[gems[start]] = check.get(gems[start],0) -1 
            if check[gems[start]] == 0:
                del check[gems[start]]
            if not check:
                break
            
            start+=1
        end += 1

    
    return answer