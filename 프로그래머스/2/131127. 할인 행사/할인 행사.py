def solution(want, number, discount):
    answer = 0
    
    # 원하는 제품과 수량을 딕셔너리로 저장
    want_dict = {}
    for i in range(len(want)):
        want_dict[want[i]] = number[i]
    
    # 가능한 각 시작일에 대해 체크
    for start in range(len(discount) - 9):
        # 10일간의 할인 제품을 카운트
        discount_dict = {}
        for i in range(start, start + 10):
            product = discount[i]
            discount_dict[product] = discount_dict.get(product, 0) + 1
        
        # 원하는 제품/수량과 일치하는지 확인
        if want_dict == discount_dict:
            answer += 1
    
    return answer