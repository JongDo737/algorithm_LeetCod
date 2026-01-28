import math
def solution(arr):
    answer = 0
    
    g = arr[0]
    for i in range(1,len(arr)):
        print(g)
        g = g * arr[i] // math.gcd(g,arr[i])
        
    print(g)
    
    return g