# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.helper(head,None)
    
    def helper(self,head,prev):
        if head == None:
            return prev
        cur = head
        head = head.next
        cur.next = prev
        return self.helper(head,cur)