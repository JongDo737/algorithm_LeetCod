from itertools import product

def solution(user_id, banned_id):
    answer = 0
    bannen_count = [[] for _ in range(len(banned_id))]
    check = True
    for ban_index in range(len(banned_id)):
        for user in user_id:
            check = False
            if len(user) == len(banned_id[ban_index]): # 일단 길이가 같아야함.
                # 비교 코드
                for i in range(len(user)):
                    # print('비교',banned_id[ban_index][i],user[i] )
                    if banned_id[ban_index][i] == '*':
                        # print(1111)
                        check = True
                        continue
                    elif banned_id[ban_index][i] == user[i]:
                        # print(2222)
                        check = True
                        continue
                    else:
                        # print(3333)
                        check = False
                        break
            if check:
                # print('추가 완 !',banned_id[ban_index], user)
                bannen_count[ban_index].append(user)
    
    # print(bannen_count)
    
    result = set()
    
    for combinations in product(*bannen_count): # 모든 경우의 수를 작업
        # print(combinations)
        if len(combinations) == len(set(combinations)):
            result.add(tuple(sorted(combinations))) # 정렬 후 set에 삽입
                
                
    
    return len(result)