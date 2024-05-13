class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [1] * n
        
        # 왼쪽 곱을 result 배열에 저장
        left_product = 1
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        # 오른쪽 곱을 이용해 결과 배열 업데이트
        right_product = 1
        for i in range(n-1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result