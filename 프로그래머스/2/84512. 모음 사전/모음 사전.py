def solution(word):
    answer = 0
    #
    # 1번째 : 1 782(1+ 5*6*6*6) 1563 2346 3128
    # 2번째 : 1 
    # 3번째 : 1 32 (1 +5*6 +1) (1+ (5*6+1) *2)
    # 4번째 : 1 7(1+ 6) 13(1+ (5*1+1)*2) 19(1+ 6*3) 25(1*6*4)
    # 5번째 : 1 2 3 4 5 
    
    # AAA 3
    # AAAA AAAE AAAI AAAO AAAU
    # 4     10   16   22   28 + 6
    #AAA AAE   AAI   AAO AAU 29+5*5+1
    # 3    34   55    81  107
    # AA AE   AI  AO AU
    #  2 108 214 320 426
    # A    E    I O U
    # 1 427
    
    weight = [781, 156, 31, 6, 1]
    w = 'AEIOU'
    
    for i in range(len(word)):
        # print(w.index(word[i]), weight[i], 1+ w.index(word[i]) * weight[i])
        answer += 1+ w.index(word[i]) * weight[i]
    
    return answer