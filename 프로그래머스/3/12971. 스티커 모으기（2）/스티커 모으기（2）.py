def solution(sticker):
    n = len(sticker)
    
    # 예외 처리
    if n == 1:
        return sticker[0]
    if n == 2:
        return max(sticker[0], sticker[1])
    
    # 첫 번째 스티커를 선택하는 경우 (마지막 스티커는 선택 불가)
    dp1 = [0] * (n - 1)
    dp1[0] = sticker[0]
    dp1[1] = max(sticker[0], sticker[1])
    
    for i in range(2, n - 1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + sticker[i])
    
    # 첫 번째 스티커를 선택하지 않는 경우 (마지막 스티커 선택 가능)
    dp2 = [0] * n
    dp2[1] = sticker[1]
    dp2[2] = max(sticker[1], sticker[2])
    
    for i in range(3, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + sticker[i])
    
    # 두 경우 중 최댓값 반환
    return max(dp1[n-2], dp2[n-1])