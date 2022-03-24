# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.a = []
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.preorder(root)
        return self.a
        
    def preorder(self, curr):
        if(curr ==  None):
            return
        self.a.append(curr.val)
        self.preorder(curr.left)
        self.preorder(curr.right)
    