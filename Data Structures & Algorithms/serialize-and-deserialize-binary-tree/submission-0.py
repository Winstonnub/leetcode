# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []
        def dfs(node): # Given a node, push itself to the string, then push the left and right subtrees (Pre-order)
            # Base Case: If we reach none
            if not node:
                res.append("N")
                return
            left, right = node.left, node.right
            res.append(str(node.val))
            dfs(left)
            dfs(right)
        dfs(root)
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        # data = "1,2,3,N,N,4,5"
        vals = data.split(",") # vals = ["1", "2,", "N",...]
        self.i = 0 # Pointer to the current val in vals being processed
        def dfs():
            value = vals[self.i]
            if value == "N":
                self.i += 1
                return None
            node = TreeNode(int(value)) # node.val defined, node.left / right is None
            self.i += 1
            node.left = dfs() # itself will move i to next number
            node.right = dfs() # itself will move i to next number
            return node
        return dfs()


# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))