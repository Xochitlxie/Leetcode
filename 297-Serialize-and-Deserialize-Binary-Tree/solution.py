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
                val.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                val.append("#")
        val = []
        doit(root)
        return " ".join(val)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def doit():
            node = next(vals)
            if node == "#":
                return None
            root = TreeNode(int(node))
            root.left = doit()
            root.right = doit()
            return root
        vals = iter(data.split(" "))
        return doit()
        
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))