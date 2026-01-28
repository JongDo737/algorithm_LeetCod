def solution(numbers):
    answer = ''
    s_list = [str(i) for i in numbers]
    
    def cmp_ab(a,b):
        return int(b+a) - int(a+b)
    s_list = sorted(s_list, cmp=cmp_ab)
    # print(s_list)
    
    answer = ''.join(s_list)
    
    # 모든 숫자가 0인 경우 처리
    if answer[0] == '0':
        return '0'
    
    return answer