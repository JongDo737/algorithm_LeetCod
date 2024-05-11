class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int

        코드를 빗물 관점에서 짜보자
        """
        if not height:
            return 0
    
        n = len(height)
        max_height_index = height.index(max(height))
        water_trapped = 0

        # 왼쪽 부분 처리
        left_max = 0
        for i in range(max_height_index):
            if height[i] > left_max:
                left_max = height[i]
            water_trapped += left_max - height[i]

        # 오른쪽 부분 처리
        right_max = 0
        for i in range(n-1, max_height_index, -1):
            if height[i] > right_max:
                right_max = height[i]
            water_trapped += right_max - height[i]

        return water_trapped