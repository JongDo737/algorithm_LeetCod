def solution(n, words):
    answer = []
    
    dict_word = {}
    # dict 사용
    dict_word[words[0]] = 1
    for index in range(1,len(words)):
        # 앞뒤 글자가 다를 때 
        if len(words[index]) == 1:
            return [index%n +1, (index // n) + 1 ]
        if words[index-1][-1] != words[index][0]:
            return [index%n +1, (index // n) + 1 ]
        
        # 이미 말한 단어
        if dict_word.get(words[index],0) == 0:
            dict_word[words[index]] = 1
        else:
            # 3 = 5 / 2 + 5 % 2
            return [index%n +1, (index // n) + 1 ]
    return [0,0]