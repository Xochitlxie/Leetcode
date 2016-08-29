import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = node = ListNode(None)
        h = [(n.val,n) for n in lists if n]
        heapify(h)
        while h:
            v,n = h[0]
            if n.next is None:
                heapq.heappop(h)
            else:
                heapq.heapreplace(h,(n.next.val,n.next))
            node.next = n
            node = node.next
       
        return dummy.next