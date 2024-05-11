class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int

        코드를 빗물 관점에서 짜보자
        """
        left_max_height, right_max_height = -1, -1
        left_max_height_index,right_max_height_index = -1, -1
        volumes = 0

        # 빗물이 고이지 않는 경우
        if len(height) <= 2:
            return 0
        
        # 양옆 미리 채워두기
        if height[0] < height[1]:
            height[0] = height[1]
        if height[len(height)-1] < height[len(height)-2]:
            height[len(height)-1] = height[len(height)-2]

#----------------------------왼쪽부터--------------------------------
        for i in range(1, len(height) -1):

            # max 벽의 같은 크기나 더 큰 크기가 나올 때 까지 기다렸다가 그 사이의 넓이 * MAX HEIGHT 해주고, 사이 값들을 빼주면 된다.
            # 이때 벽 값은 다시 0으로
            # 마지막 끝났을 땐 남은 것들 확인해줘야함.

            # 왼쪽 max 기둥 계산
            if left_max_height <= height[i-1]:
                left_max_height = height[i-1]
                left_max_height_index = i-1
            # 오른쪽 max 기둥 계산
            if right_max_height <= height[i+1]:
                right_max_height = height[i+1]
                right_max_height_index = i+1
            
            # 연속 max 기둥 차단 287번
            if left_max_height_index == right_max_height_index:
                right_max_height = -1
                right_max_height_index = -1
                continue

            # 수영장이 만들어 졌을 때 
            if left_max_height <= right_max_height and left_max_height_index < right_max_height_index:
                
                if height[i] >= height[i+1]:
                    left_max_height = height[i]
                    continue
                # 왼벽과 오른벽 둘중 작은게 물 높이
                rain_height = min(left_max_height, right_max_height)
                rain_width = i - left_max_height_index
                blocks = sum(min(block, rain_height) for block in height[left_max_height_index+1:i+1])
                if ( rain_height * rain_width ) >= blocks:
                    volumes += ( rain_height * rain_width ) - blocks

                # 계산된 수영장은 시멘트로 채우기
                for j in range(left_max_height_index+1,i+1):
                    if height[j] < rain_height:
                        height[j] = rain_height

                left_max_height = -1
                right_max_height = -1

        # 내리막 고인물 처리
        if left_max_height != -1 and right_max_height != -1:
            rain_height = min(left_max_height, right_max_height)
            rain_width = right_max_height_index-1 - left_max_height_index
           

            #209 테스트 케이스 실패 : 수영장을 만들고 높이보다 개별 block 높이가 크면 안됌
            # min() 추가
            blocks = sum(min(block, rain_height) for block in height[left_max_height_index+1 : right_max_height_index])

            # 189 테스트 케이스 2 : 볼륨이 마이너스가 될 상황 처리
            if ( rain_height * rain_width ) >= blocks:
                volumes += ( rain_height * rain_width ) - blocks
             # 계산된 수영장은 시멘트로 채우기
            for j in range(left_max_height_index+1,right_max_height_index):
                if height[j] < rain_height:
                    height[j] = rain_height

#----------------------------오른쪽부터--------------------------------
        
        last_left, last_right = left_max_height_index, right_max_height_index 
        left_max_height, right_max_height = -1, -1
        left_max_height_index,right_max_height_index = -1, -1

        for i in range(1, len(height)-1):
            i = len(height) - i - 1

            # 왼쪽 max 기둥 계산
            if left_max_height <= height[i-1]:
                left_max_height = height[i-1]
                left_max_height_index = i-1
            # 오른쪽 max 기둥 계산
            if right_max_height <= height[i+1]:
                right_max_height = height[i+1]
                right_max_height_index = i+1

            # 수영장이 만들어 졌을 때 
            if right_max_height <= left_max_height :
                
                if height[i] >= height[i-1]:
                    right_max_height = height[i]
                    continue
                # 왼벽과 오른벽 둘중 작은게 물 높이
                rain_height = min(left_max_height, right_max_height)
                rain_width = right_max_height_index - i
                blocks = sum(min(block, rain_height) for block in height[i:right_max_height_index])
                if ( rain_height * rain_width ) >= blocks:
                    volumes += ( rain_height * rain_width ) - blocks
                left_max_height = -1
                right_max_height = -1

            
        return volumes