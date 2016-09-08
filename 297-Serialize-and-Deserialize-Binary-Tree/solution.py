# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def doit(node):
            if node:
                val.append(node.val)
                doit(node.left)
                doit(node.right)
            else:
                val.append("#")
        val = []
        doit(node)
        return " ".join(vals)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def doit(vals):
            node = next(vals)
            if node == "#":
                return None
            root = TreeNode(int(node.val))
            root.left = doit()
            root.right = doit()
            return node
        vals = iter(data.split(" "))
        return doit(vals)
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))