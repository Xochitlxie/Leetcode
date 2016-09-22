# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(0)
        dummy = head
        while l1 != None or l2 != None:
            if not l1:
                sumVal = l2.val + carry
                l2 = l2.next
            elif not l2:
                sumVal = l1.val + carry
                l1 = l1.next
            else:
                sumVal = carry + l1.val + l2.val
                l1,l2 = l1.next,l2.next
            dummy.next = ListNode(sumVal%10)
            carry = sumVal/10
            dummy = dummy.next
        if carry:
            dummy.next = ListNode(carry)
        return head.next