# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        queue = deque([[root, -float('inf'), float('inf')]])
        while queue:
            node, lowerbound, upperbound = queue.popleft()
            if not (lowerbound < node.val < upperbound):
                return False
            if node.left:
                queue.append((node.left, lowerbound, node.val))
            if node.right:
                queue.append((node.right, node.val, upperbound))
        return True
            
