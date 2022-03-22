# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.a = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.inorder(root)
        return self.a
        
    def inorder(self, curr):
        if(curr == None):
            return
        self.inorder(curr.left)
        self.a.append(curr.val)
        self.inorder(curr.right)