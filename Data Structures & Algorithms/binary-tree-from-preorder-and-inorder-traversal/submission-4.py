# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #Preorder [3,9,20,15,7]
        #inorder [9,3,15,20,7]
        # Alg:
        # 1. preorder[0] is always the new root
        # 2. find preorder[0] index in inorder set that to mid.
        # 3. left of mid is smaller, right of mid is larger
        # 4. e.g. we know left = 1, right = 3. Then we left is 9, right is 20,15,7
        # 5. We recurisvely call buildTree with two new list for left and right
        # For left: preorder is 9 so [1, mid+1], inorder is 9 so [:mid]
        # For right: preorde ris 20,15,7 so [mid+1:] , in order is 20,15,7 so [mid+1:]
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0]) # we are builing!
        mid = inorder.index(preorder[0])
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        return root