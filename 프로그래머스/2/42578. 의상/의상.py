from collections import Counter
def solution(clothes):
    answer = 1
    # clothes.append(["blue_one", "eyewear"])
    clothes_types = []
    
    for types in clothes:
        clothes_types.append(types[-1])
    
    clothes_types = Counter(clothes_types)
    
    list1 = list(clothes_types.values())
    for count in list1:
        answer *= (count+1)
        
    return answer -1