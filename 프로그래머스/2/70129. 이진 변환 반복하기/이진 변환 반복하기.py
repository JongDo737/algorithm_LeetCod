def solution(s):
    count = 0
    count_zero = 0
    while True:
        if s == '1':
            break
        a = len(s)
        s = s.replace('0','')
        b = len(s)
        
        
        s = format(len(s), 'b')
        count_zero += a-b
        count += 1
    
    return [count, count_zero]