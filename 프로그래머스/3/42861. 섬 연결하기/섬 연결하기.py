def solution(n, costs):
    answer = 0
    # [ [섬노드1,섬노드2,비용] ... ]
    answer_list = []
    
    visited = [False] * (n)
    
    g = [[] for _ in range(n)]
    for u,v,c in costs:
        g[u].append([v,c])
        g[v].append([u,c])
    # print(g)
    
    cost_list = []
    
    # 해당 노드와 연결되어있는 노드들과 가격 추가
    # 가장 싼 노드 출발
    
    def insert_node(c):
        for v,cost in g[c]:
            if not visited[v]:
                cost_list.append([v,cost])
        cost_list.sort(key=lambda x: x[1]) # cost 정렬
    
    index = costs[0][0]
    while len(answer_list) < n-1:
        visited[index] = True
        insert_node(index)
        print(cost_list)
        
        for _ in cost_list:
            if not visited[cost_list[0][0]]:
                
                answer_list.append(cost_list[0][1])
                index = cost_list[0][0]
                del cost_list[0]
                break
            else:
                del cost_list[0]

    
        print(answer_list)
    
    return sum(answer_list)