import math
def solution(n):
    answer = 1
    # 1111 -> 1 1 2 -> 2 2
    # 4C0 -> 3C2 -> 2C2 계산해서 합계
    # 5C2 = 5! / 3! / 2! 하믄댐
    num_1 = n
    num_2 = 0
    while(num_1 >= 2):
        
        num_1 -= 2
        num_2 += 1
        
        answer += math.factorial(num_1+num_2) / math.factorial(num_2) / math.factorial(num_1)
        
    return answer % 1234567