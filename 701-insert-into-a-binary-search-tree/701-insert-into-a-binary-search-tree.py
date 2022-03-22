# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if(root == None):
            root = TreeNode(val)
            return root
        self.insert(root, val)
        return root
        
    def insert(self, curr, val):
        
        if(val < curr.val):
            if(curr.left == None):
                curr.left = TreeNode(val)
                return
            return self.insert(curr.left, val)
        else:
            if(curr.right == None):
                curr.right = TreeNode(val)
                return
            return self.insert(curr.right, val)
        
        
        