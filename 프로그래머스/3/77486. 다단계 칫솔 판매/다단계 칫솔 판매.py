def solution(enroll, referral, seller, amount):
    answer = []
    
    # 자신의 칫솔 판매 이익 + 아래 판매원 이익 10% - 자신의 추천인 10 %
    # int 이고, 판매 수익이 10원 아래면 본인이 가진다.
    
    def money_calc(seller_name, amount_value):
        # print(seller_name, amout_value)
        if int(amount_value // 10) < 1:
            _dict[seller_name] = _dict.get(seller_name,0) + amount_value
            return
        if seller_name == '-':
            return
        amount_value // 10

        _dict[seller_name] = _dict.get(seller_name,0) + amount_value - int(amount_value // 10)
        # print(_dict)
        money_calc(_dict_referral[seller_name], amount_value // 10)
        
    
    _dict = {}
    _dict_referral = {}
    
    for i in range(len(enroll)):
        _dict[enroll[i]] = 0
        _dict_referral[enroll[i]] = referral[i]
        
    # print(_dict)
    
    for i in range(len(seller)):
        money_calc(seller[i], amount[i]* 100)
        # print('--------------')
    

    for i in range(len(enroll)):
        answer.append(_dict[enroll[i]])
    
    return answer