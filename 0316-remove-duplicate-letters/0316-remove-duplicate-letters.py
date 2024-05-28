import collections
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter, seen, stack = collections.Counter(s), set(), []

        print(counter)
        
        for char in s:
            # 해당 문자열 Counter -1
            counter[char] -= 1

            # 중복된 숫자 제거
            if char in seen:
                continue

            # 뒤에 붙일 숫자 있는지 확인
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            
            stack.append(char)
            seen.add(char)

        return ''.join(stack)