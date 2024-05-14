class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        min_num = 100000
        max_num = 0
        for i in range(0,len(prices)):

            if prices[i] > max_num:
                max_num = prices[i]
                if (max_num - min_num) > result:
                    result = max_num - min_num
                
            # 작은 수가 나왔을 때, max_num은 초기화 되야한다.
            if prices[i] < min_num:
                min_num = prices[i]
                max_num = 0
        return result
            