# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        node = ListNode(0)
        cur = node
        now_value = -101

        while(head is not None):
            # print(head.val, now_value, cur.val)
            if(head.val != now_value):
                # 현재 값 넣기
                # print(head.val)
                cur.next = head
                cur = cur.next
                now_value = cur.val

            # head 다음 값
            head = head.next
            # 반드시 넣어서 꼬리 짜르기
            cur.next = None
        return node.next

            
            


        