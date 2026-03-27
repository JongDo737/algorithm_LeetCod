from collections import Counter
def solution(topping):
    answer = 0
    
    right_dict = Counter(topping)
    print(right_dict)
    left_dict = {}
    
    left_type = 0
    right_type = len(set(topping))
    
    for t in topping:
        
        # 왼쪽 토핑 추가
        if t not in left_dict:
            left_dict[t] = 1
            left_type += 1
        else :
            left_dict[t] +=1
        
        # 오른쪽 토핑 제거
        if right_dict[t] > 1:
            right_dict[t] -= 1
        else:
            del right_dict[t]
            right_type -= 1
        
        # print(left_dict,left_type, right_dict, right_type)
        
        if left_type == right_type:
            answer += 1
    
    
    return answer