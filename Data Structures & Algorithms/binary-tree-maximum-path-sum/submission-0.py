# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        # Idea: Tree DP (Post Order DFS with global answer, post order means children then parent) (DP to keep track of best connectable path by its parents), one global variable to store best result
        # DFS: return the max path sum that can be continued (left + root, right + root, root)
        # Best: what is the best local max path sum (can be bent)? max(best, root + left + right)
        # Clip left and right to be at least 0
        best = float("-inf")
        
        def dfs(node): # the max path sum of this node that is still extendable by its parent
            nonlocal best
            if not node:
                return 0
            left, right = dfs(node.left), dfs(node.right)
            left_value, right_value = max(0, left), max(0, right)
            # Only extendable if [left+node, right+root, root]
            best = max(best, node.val + left_value + right_value)
            return max(node.val + left_value, node.val + right_value, node.val)
        dfs(root)
        return best
