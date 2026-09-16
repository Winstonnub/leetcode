# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # We can do a BFS each layer
        # In each layer, we keep track of the largest we have seen (augment!)
        res = 0
        q = deque() # current, largest we have ever seen
        q.append((root, root.val))
        while q:
            for i in range(len(q)):
                curr, largest = q.popleft()
                if curr.val >= largest:
                    res += 1
                largest = max(curr.val, largest)
                if curr.left: q.append((curr.left, largest))
                if curr.right: q.append((curr.right, largest))
        return res


        