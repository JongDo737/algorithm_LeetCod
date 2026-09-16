from collections import deque

def solution(s):
    answer = True
    
    stack = deque()
    left = ['(','[','{']
    right = [')',']','}']
    
    if s[0] in right:
        return False
    
    if len(s) % 2 == 1:
        return False
    
    for c in s:
        if c in left:
            stack.append(c)
            
        else:
            if not stack:
                return False
            # 비교
            left_one = stack.popleft()
            
            
            if left_one == '(':
                if c != ')':
                    return False
                
            elif left_one == '[':
                if c != ']':
                    return False
            else:
                if c != '}':
                    return False
                
    if len(stack) > 0:
        return False
    
    return answer