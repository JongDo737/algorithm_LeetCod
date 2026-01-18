class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 전체 개수 - 중복 카운트 개수
        temp = -101
        count = 0
        i = 0
        while i < len(nums):
            if nums[i] == '_':
                break
            if nums[i] > temp:
                temp = nums[i]
                i += 1
            else:
                nums.pop(i)
                nums.append('_')
                count += 1
        
        return len(nums) - count
            