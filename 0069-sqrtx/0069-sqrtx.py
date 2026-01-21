class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # 2진 정렬로 찾아서 제곱해보고 소수점이나 x값이 나오면 종료
        # 9일때 4.5제곱이 9 이하면 2.25 
        # 2.25 제곱이 9 이상이면 (pivot+x)/2 를 제곱 
        # p1:최소 p2:현재 p3:최대
        p1 = 0
        p2 = x/2
        p3 = x

        if x <= 1:
            return x

        while(True):
            print("p :",p1,p2,p3)
            int_p2 = int(p2)
            sqrt = int_p2 * int_p2
            sqrt_plus = (int_p2+1) * (int_p2+1)
            if sqrt == x or (sqrt<x and sqrt_plus > x) :
                return int_p2

            if (p2*p2) > x: # 클 경우
                p3 = p2
                p2 = (p1+p2) / 2
            else:           # 작을 경우
                p1 = p2
                p2 = (p1+p3) / 2

        