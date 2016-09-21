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
            if l1 == None:
                sumVal = carry + l2.val
            elif l2 == None:
                sumVal = carry + l1.val
            else:
                sumVal = carry + l1.val + l2.val
            dummy.next = ListNode(sumVal%10)
            carry = sumVal/10
            dummy,l1,l2 = dummy.next,l1.next,l2.next
        return head.next