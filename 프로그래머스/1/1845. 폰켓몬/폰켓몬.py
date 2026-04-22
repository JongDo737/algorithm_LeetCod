from collections import Counter
def solution(nums):
    answer = 0
    
    dict = Counter(nums)
    
    types = list(dict.keys())
    
    if len(types) > (len(nums) / 2):
        return len(nums) / 2
    else:
        return len(types)
    
    