from collections import deque
def solution(tickets):
    
    # 정렬
    tickets.sort()
    visited = [False] * len(tickets)
    answer = []
    
    def dfs(current, path):
        # 경로가 끝나면 종료
        if len(path) == len(tickets) + 1:
            answer.append(path[:])
            return True
        
        for i, (start, end) in enumerate(tickets):
            if not visited[i] and start == current:
                visited[i] = True
                # 경로가 끝날때까지 반복
                if dfs(end, path + [end]):
                    return True # 성공한 경로를 찾으면 즉시 종료
                # 막다른 길이면 경로 취소
                visited[i] = False
        # 현재 위치에서 더 이상 갈 곳이 없으면 False 반환
        return False
    
    # ICN 부터 출발
    dfs("ICN", ["ICN"])
    return answer[0] if answer else []