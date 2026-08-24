# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        #DFS (can use BFS)
        stack = [root]
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node.val == subRoot.val:
                if self.sameTree(node, subRoot):
                    return True
            stack.append(node.right)
            stack.append(node.left)
        return False



    def sameTree(self, root1, root2): # as from last question, recursive
        # two empty root
        if not root1 and not root2:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        # Recursive implemetation
        if self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right):
            return True