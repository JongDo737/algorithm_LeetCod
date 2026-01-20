class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # check를 통해 다음 수 올리기
        return format(int(a,2) + int(b,2),"b")
        