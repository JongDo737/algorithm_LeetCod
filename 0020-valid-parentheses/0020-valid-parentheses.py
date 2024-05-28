class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # 홀수면 false
        if len(s) % 2 == 1: return False

        stack = []
        # 짝수일 경우
        for i in range(0,len(s)): 
            if s[i] in ['(','[','{']:
                stack.append(s[i])
            else:
                # 닫는게 나왔는데 아무것도 없을 때
                if len(stack) == 0:
                    # print('111')
                    return False
                # 닫는게 짝이 안맞을 때
                if (s[i] == ')' and stack.pop() != '(') or (s[i] == '}' and stack.pop() != '{') or (s[i] == ']' and stack.pop() != '[') :
                    return False
                
            # print(stack)

        return len(stack) == 0