# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # DFS Solution (In order traversal with DFS always give sorted array)
        arr = []
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)

        dfs(root)
        return arr[k-1]


        ''' #Brute Force
        if not root:
            return 0
        queue = deque([root])
        arr = []

        while queue:
            node = queue.popleft()
            arr.append(node.val)
            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)
        arr.sort()
        return arr[k-1]
        '''