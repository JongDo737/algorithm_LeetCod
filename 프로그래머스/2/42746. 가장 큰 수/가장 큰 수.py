from functools import cmp_to_key
def solution(numbers):
    answer = ''
    
    s_list = [str(i) for i in numbers]
    
    # print(s_list)
    
    def cmp_ab(a,b):
        return int(a+b) - int(b+a)
    
    s_list = sorted(s_list , key=cmp_to_key(cmp_ab), reverse=True)
    
    # print(s_list)
    
    answer = ''.join(s_list)
    
    return str(int(answer))