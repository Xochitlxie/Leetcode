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
        larger = listNode("l")
        newHead = small
        lHead = larger
        if not head:
            return head
        while head != None:
            if head.val < x:
                small.next = head
                small = small.next
                small.next = None
            else:
                larger.next = head
                larger = larger.next
                larger.next = None
            head = head.next
        small.next = lHead.next
        return newHead.next