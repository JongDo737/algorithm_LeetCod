from collections import Counter
def solution(nums):
    answer = 0
    set1 = set(nums)
    if len(set1) > (len(nums) / 2):
        return len(nums) / 2
    else:
        return len(set1)
    
    