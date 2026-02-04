def solution(A, B):
    answer = 0
    
    A.sort(reverse=True)
    B.sort(reverse=True)
    
    index_a = 0
    index_b = 0
    while index_a < len(A) and index_b < len(B):
        if A[index_a] >= B[index_b]:
            index_a += 1
        else:
            answer+=1
            index_a += 1
            index_b += 1
        
    
    return answer