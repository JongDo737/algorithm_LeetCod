def solution(n):
    ans = 0
    
    while n > 0:
        if n % 2 == 1:  # 홀수면 점프가 필요했던 것
            ans += 1
            n -= 1
        else:           # 짝수면 순간이동으로 온 것 (무료)
            n //= 2
    
    return ans