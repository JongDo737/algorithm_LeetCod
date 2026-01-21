# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 노드 초기화
        node = ListNode(0)
        cur = node

        # 10의 배수 설정
        i = 1
        l1_num = 0
        l2_num = 0
        while(l1 or l2):
            if l1 is not None:
                 l1_num += l1.val * i
                 l1 = l1.next
            if l2 is not None:
                 l2_num += l2.val * i
                 l2 = l2.next
            i *= 10
        # 합계
        result = str(l1_num + l2_num)
        # print(l1_num, l2_num, result)
        for j in result[::-1]: # 54321
            # print(j)
            cur.next = ListNode(int(j))
            cur = cur.next
        return node.next



