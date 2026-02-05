def solution(n, s):
    answer = []
    
    if n > s :
        return [-1]
    
    # 큐 생성
    sum = int(s/n) * n
    
    for i in range(n-(s-sum)):
        answer.append(int(s/n))
    
    for i in range(s-sum):
        answer.append(int(s/n)+1)
    
    
    
    return answer