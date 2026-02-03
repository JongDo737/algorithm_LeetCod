from collections import deque

def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    # BFS 풀기
    def transform_check(word1, word2):
        length_check = True
        for i in range(len(word1)):
            if word1[i] != word2[i] and length_check:
                length_check = False
            elif word1[i] != word2[i] and not length_check:
                return False
        return True
    
    queue = deque()
    queue.append([begin,0])
    visited = [False] * len(words)
    while queue:
        v,step = queue.popleft()
        print(v)
        answer += 1
        if v == target:
            return answer
        for i in range(len(words)):
            if not visited[i] and transform_check(v, words[i]):
                
                if words[i] == target:
                    return step +1
                visited[i] = True
                queue.append([words[i],step+1])
    
    
    return answer