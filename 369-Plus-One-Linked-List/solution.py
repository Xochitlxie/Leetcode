# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        i = dummy
        j = dummy
        
        while i.next != None:
            i = i.next
            if i.val != 9:
                j = i
        
        if i.val != 9:
            i.val += 1
        else:
            j.val += 1
            j = j.next
            while j != None:
                j.val = 0
                j = j.next
        
        if dummy.val != 0:
            return dummy
        else:
            return dummy.next