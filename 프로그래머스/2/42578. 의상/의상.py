def solution(clothes):
    answer = 1
    # 의상의 종류를 먼저 파악
    # 총개수 + 곱하기  // 굳이 총개수 안하고 종류+1개로 곱셈하고 -1 하면 되는거 아녀 ?
    type = []
    for i in range(len(clothes)):
        type.append(clothes[i][1])
    type = list(set(type))
    
    count = [0] * len(type)
    for i in range(len(clothes)):
        count[type.index(clothes[i][1])] += 1
    # print(type)
    
    for i in range(len(count)):
        answer *= count[i]+1
        
        
    
    return answer-1