def solution(s):

    stack = []  # list가 파이썬에서 스택으로 가장 빠름
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return 1 if not stack else 0
