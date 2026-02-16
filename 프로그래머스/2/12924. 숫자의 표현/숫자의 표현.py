def solution(n):
    answer = 0
    min_num = 1
    max_num = 1
    _sum = 0

    while min_num <= n:
        if _sum < n:
            _sum += max_num
            max_num += 1
        elif _sum > n:
            _sum -= min_num
            min_num += 1
        else:
            answer += 1
            _sum -= min_num
            min_num += 1

    return answer
