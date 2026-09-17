# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # It is a good node if current largest is smaller than itself
        res = 0
        q = deque()
        q.append((root, root.val))
        largest = 0
        while q:
            for i in range(len(q)):
                curr, largest = q.popleft()
                if largest <= curr.val:
                    res += 1
                largest = max(largest, curr.val)
                if curr.left: q.append((curr.left, largest))
                if curr.right: q.append((curr.right, largest))
        return res
