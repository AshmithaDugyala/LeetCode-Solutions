# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        """temp=head
        while temp.nextis not None :
            if temp.val==val:
                temp.next=temp.next.next
                continue
        temp=temp.next
        return head.next"""


        dummy=ListNode(0)
        dummy.next=head
        temp=dummy
        while temp.next is not None:
            if temp.next.val==val:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return dummy.next