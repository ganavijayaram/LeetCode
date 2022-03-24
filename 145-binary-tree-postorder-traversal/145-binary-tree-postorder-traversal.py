# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.a = []
        
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.post(root)
        return self.a
        
    def post(self, curr):
        if(curr == None):
            return
        self.post(curr.left)
        self.post(curr.right)
        self.a.append(curr.val)