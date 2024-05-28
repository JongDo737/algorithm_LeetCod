class Solution(object):
    def dailyTemperatures(self, temperatures):

        # 본인 기준 다음 리스트에서 높은 수까지의 인덱스 거리를 구하면 되는 문제인거 같음.
        # 투포인터 해보자
        answer = [0] * len(temperatures)
        stack = []

        for i in range(0,len(temperatures)):
            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)

        return answer