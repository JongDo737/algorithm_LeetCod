def solution(n):
    count = bin(n).count('1')  # n의 1의 개수
    
    next_n = n + 1
    while True:
        if bin(next_n).count('1') == count:
            return next_n
        next_n += 1