# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS, use a queue
        res = []
        q = deque([root])
        while q:
            rightSide = None
            qLen = len(q) # the current level's size
            for i in range(qLen): # Only for inital length!
                node = q.popleft()
                if node:
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide:
                res.append(rightSide.val) #at the end of for loop, rightSide is rightmost since if None we wont set it to rightSide
        return res




        