class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        

        nums = sorted(nums)
        arr = []
        # print(nums)
        for i in range(len(nums)-2):

            # 중복 값 차단
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1

            while left < right:
                # 투포인터 조작
                # print(nums[i],nums[left],nums[right])
                # 중복된 수 차단
                if left > i+1 and nums[left] == nums[left-1]:
                    left += 1
                    continue
                if right < len(nums)-1 and nums[right] == nums[right+1]:
                    right -= 1
                    continue

                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else :
                    # if not in 
                    arr.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1

            

        return arr