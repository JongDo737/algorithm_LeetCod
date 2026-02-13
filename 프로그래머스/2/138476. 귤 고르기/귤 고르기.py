def solution(k, tangerine):
    answer = 0
    
    # _list[크기] = 개수
    # 큰거 부터 차례로
    
    _dict = {}
    
    for size in tangerine:
        _dict[size] = _dict.get(size, 0) + 1
    
    _list = sorted(list(_dict.values()))
    
    for i in _list[::-1]:
        if k <= 0:
            return answer
        # print(k, i)
        k -= i
        answer += 1
    
    return answer