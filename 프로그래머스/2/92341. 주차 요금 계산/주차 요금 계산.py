import math
from functools import cmp_to_key
def solution(fees, records):
    answer = []
    # 요금 계산 
    record_list = [] # [차량][시간]
    # {
    #     [0] = ["5961", "05:34"]
    #     [1] = ["0000", "06:00"]
    # }
    
    answer_list = [] # [차량][시간]
    # {
    #     [0] = ["5961", 145]
    #     [1] = ["0000", 366]
    # }
    price_list = [] # [차량][금액] -> 정렬 필요 !!!
    # {
    #     [0] = ["5961", 14600]
    #     [1] = ["0000", 34400]
    # }
    
    # records 반복문
    # IN일 경우 record_list에 삽입
    # OUT일 경우 출차로 간주해서 요금 계산
    # 반복문 종료 후 record_list 남은 차는 23:59로 계산
    
    # 시간 계산 (입차시간, 출차시간)
    def count_time(before, after):
        # HH:MM 
        b_list = before.split(':') 
        a_list = after.split(':')
        return 60 * (int(a_list[0])-int(b_list[0])) + (int(a_list[1])-int(b_list[1]))
    
    # 금액 계산 (주차 시간)
    def count_price(time):
        price = 0
        # 기본 요금 계산
        price += fees[1]
        time -= fees[0]
        # 추가 요금 계산
        if time > 0:
            price += math.ceil(time / fees[2]) * fees[3]
        return price
    
    # 리스트 정렬
    def comp(list1,list2):
        return int(list1[0]) - int(list2[0])
        
    for i in range(len(records)):
        temp = records[i].split()  
        
        if records[i][-1] == 'N': # IN
            record_list.append([temp[1],temp[0]])
        else: # OUT
            index = 0
            for j in range(len(record_list)):
                if record_list[j][0] == temp[1]:
                    index = j
                    break
            # 시간 계산
            time = count_time(record_list[index][1], temp[0])
            
            # 시간 추가
            index2 = -1
            for j in range(len(answer_list)):
                if answer_list[j][0] == temp[1]:
                    index2 = j
                    break
            if index2 == -1:
                answer_list.append([temp[1],time])
            else:
                # 있다면 기존값에 요금 추가
                answer_list[index2] = [temp[1], answer_list[index2][1]+time]
            # 주차장에서 차량 제거 
            del record_list[index]
    if record_list:
        for i in range(len(record_list)):
            time = count_time(record_list[i][1], '23:59')
            # 시간 추가
            index2 = -1
            for j in range(len(answer_list)):
                if answer_list[j][0] == record_list[i][0]:
                    index2 = j
                    break
            if index2 == -1:
                answer_list.append([record_list[i][0],time])
            else:
                # 있다면 기존값에 요금 추가
                answer_list[index2] = [record_list[i][0], answer_list[index2][1]+time]
            
            
    # 금액 계산
    for i in range(len(answer_list)):
        p_temp = count_price(answer_list[i][1])
        price_list.append([answer_list[i][0], p_temp])
    
    # 정렬
    # print(price_list)
    price_list = sorted(price_list, key=cmp_to_key(comp))
    for i in price_list:
        answer += [i[1]]
    return answer