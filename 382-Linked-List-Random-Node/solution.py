# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.root = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        result,n,root = self.root.val,1,self.root.next
        while root:
            j = random.randint(0,n)
            print j
            if not j:
                result = root.val
            root = root.next
            n += 1
        return result
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()