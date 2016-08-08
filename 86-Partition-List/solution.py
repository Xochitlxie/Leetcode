# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small = ListNode("s")
        larger = ListNode("l")
        newHead = small
        lHead = larger
        if not head:
            return head
        while head != None:
            if head.val < x:
                small.next = head
                small = small.next
            else:
                larger.next = head
                larger = larger.next
            head = head.next
        larger.next = None
        small.next = lHead.next
        return newHead.next