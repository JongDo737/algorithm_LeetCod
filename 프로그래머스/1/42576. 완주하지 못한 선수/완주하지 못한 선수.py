from collections import Counter 
def solution(participant, completion):
    
    dict1 = Counter(participant)
    
    dict2 = Counter(completion)
    
    answer = dict1 - dict2
    
    return list(answer.keys())[0]