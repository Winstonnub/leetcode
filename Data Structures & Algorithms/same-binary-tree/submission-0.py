# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        #BFS Traversal should be same
        p_deque = deque([p])
        q_deque = deque([q])
        while p_deque and q_deque:
            for _ in range(len(p_deque)):
                nodep = p_deque.popleft()
                nodeq = q_deque.popleft()
                if nodep is None and nodeq is None: continue
                if nodep is None or nodeq is None or nodep.val != nodeq.val: return False
                p_deque.append(nodep.left)
                p_deque.append(nodep.right)
                q_deque.append(nodeq.left)
                q_deque.append(nodeq.right)

        return True
        