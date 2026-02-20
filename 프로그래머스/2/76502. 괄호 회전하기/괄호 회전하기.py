from collections import deque
def solution(s):
    answer = 0
    queue = deque()
    # 홀수 개면 올바를 수 없음
    if len(s) % 2 == 1 :
        return 0
    
    def calc_stack(temp):
        queue.clear()
        
        for t in temp:
            # print(queue, t)
            if t == '(' or t == '[' or t == '{':
                queue.append(t)
            else:
                if not queue:
                    return False
                pop = queue.pop()
                
                if pop == '{' and t != '}':
                    return False
                elif pop == '[' and t != ']':
                    return False
                elif pop == '(' and t != ')':
                    return False
        return True
    
    for i in range(len(s)):
        # print('문자열',s)
        if calc_stack(s): # True
            answer += 1
        s+= s[0]
        s = s[1:len(s)]
    
    return answer