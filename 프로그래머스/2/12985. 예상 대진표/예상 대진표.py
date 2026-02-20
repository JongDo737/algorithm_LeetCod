def solution(n,a,b):
    answer = 0

    
    # 2의 n 승수 만큼
    count = 0
    
    while True:
        a = (a+1) // 2
        b = (b+1) // 2
        count += 1
        if a == b:
            break
    return count