# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# Idea:
# 1. We store a global variable called res as the diameter. We check from bottom up.
# 2. We do DFS to return HEIGHT. Base case is None, return 0. Else return the max of left and right's tree and + 1. 
# 3. In that loop we also update res to be the max diameter we ever seen.
# 4. Start the DFS in root.
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        #Returns a height
        def dfs(curr):
            if not curr: # reach a null
                return 0 # height is 0
            leftheight = dfs(curr.left)
            rightheight = dfs(curr.right)
            self.res = max(self.res, leftheight + rightheight) #diameter
            return max(leftheight, rightheight) + 1
        dfs(root) # after running, self.res is the answer
        return self.res

            

            

        