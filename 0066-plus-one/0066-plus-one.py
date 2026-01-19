class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # 1개일 경우
        if len(digits) == 1:
            
            num_str = str(digits[0] + 1)
            # 문자 -> 리스트
            digits = list(num_str)
            # 문자리스트 -> 숫자 리스트
            digits = list(map(int,digits))
        # 1개 이상일 경우
        else:
            num_str = ""
            for i in digits:
                num_str += str(i)
                
            num_str = str(int(num_str) + 1)
            digits = list(num_str)
            digits = list(map(int,digits))

        return digits