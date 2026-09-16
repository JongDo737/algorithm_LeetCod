from collections import Counter

def solution(str1, str2):
    answer = 0
    
    # 자카드 유사도 = 교집합 / 합집합
    # 공집합 일경우 = 1
    
    # 다중집합 생성
    a = double(str1.lower())
    b = double(str2.lower())
    
    if not a and not b:
        return 1 * 65536
    # print(a)
    # print(b)
    
    # A = {1, 1, 2, 2, 3}
    # B = {1, 2, 2, 4, 5}
    
    # A ∩ B = {1, 2, 2}
    # A ∪ B = {1, 1, 2, 2, 3, 4, 5}
    
    # Counter 사용해서 min max
    counter_a = Counter(a)
    counter_b = Counter(b)    
    
    total_list = set(a+b)
    
    # print(counter_a)
    # print(total_list)
    
    sum_a = 0
    sum_b = 0
    
    # 
    for s in total_list:
        min_num = min(counter_a[s], counter_b[s])
        max_num = max(counter_a[s], counter_b[s])
        
        sum_a += min_num
        sum_b += max_num
    
    # print(sum_a)
    # print(sum_b)
    
    answer = int((sum_a / sum_b) * 65536)
    
    return answer

def double(str1):
    a = []
    for i in range(0, len(str1)-1):
        if (str1[i] >= 'a' and str1[i] <= 'z') and (str1[i+1] >= 'a' and str1[i+1] <= 'z') :
            a.append(str1[i]+str1[i+1])
    
    return a