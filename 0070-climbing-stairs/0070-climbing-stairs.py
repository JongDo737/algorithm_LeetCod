class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 2의 개수마다 가지수를 구하고, C 계산(4C2, 9C3) 이렇게
        # 총 개수는 / 2
        count = 1
        if n == 1:
            return 1
        # 9일 때 
        if n % 2 == 1: 
            odd = 1 
            even = (n-1)/2 # 2가 4개
        else:
            odd = 0
            even = n/2

        while(odd < n):
            print(count,odd,even)
            count += math.factorial(odd+even) / math.factorial(odd) / math.factorial(even)
            odd += 2
            even -= 1

        return count