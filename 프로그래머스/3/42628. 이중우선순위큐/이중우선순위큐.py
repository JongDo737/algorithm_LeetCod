def solution(operations):
    answer = []
    sort_check = False
    # 최대한 sort 함수와 슬라이싱 활용
    for op in operations:
        operation, num = op.split(' ')
        # print(operation,num,sort_check)
        if operation == 'I':
            answer.append(int(num))
            sort_check = False
        elif answer and operation == 'D':
            # 정렬 안되어 있을 때 
            if not sort_check:
                # print('sort !')
                answer.sort()
                sort_check = True
            if num == '-1':
                answer = answer[1:]
            elif num == '1':
                answer = answer[:-1]
        # print(answer)
    if len(answer) < 1:
        answer.append(0)
    if not answer:
        return [0,0]
    
    if not sort_check:
        answer.sort()
    
    print([answer[-1], answer[0]])
    return [answer[-1], answer[0]]