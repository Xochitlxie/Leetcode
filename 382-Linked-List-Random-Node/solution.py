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
        self.reservoir = [head.val]
        self.n = 2
        self.root = head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        while self.root:
            j = random.randint(0,self.n)
            if j < 1:
                self.reservior[0] = self.root.val
            self.root = self.root.next
            self.n += 1
        return self.reservoir[0]
        
# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()