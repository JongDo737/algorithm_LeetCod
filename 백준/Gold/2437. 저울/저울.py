# 7
# 3 1 6 2 7 30 1

N = int(input())
_list = list(map(int,input().split()))
_list.sort()

target = 1

for weight in _list:
    if weight > target:
        break
    target += weight
print(target)