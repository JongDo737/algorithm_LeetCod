def solution(s):
    answer = []
    # 앞 {{ 뒤 }} 지우고 split('},{')
    _list = s[2:-2].split('},{')
    _list = [i.split(',') for i in _list]
    
    def comp(a,b):
        return len(a)- len(b)
    
    _list = sorted(_list, cmp=comp)
    # print(_list)
    # answer.append(int(_list[0][0]))
    for i in range(len(_list)):
        # answer내 없는 원소 추가하기
        for j in range(len(_list[i])):
            if int(_list[i][j]) not in answer:
                answer.append(int(_list[i][j]))
                break
                       
        
    return answer