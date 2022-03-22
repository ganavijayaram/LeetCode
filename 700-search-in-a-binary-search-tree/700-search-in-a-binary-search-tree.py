# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.search(val, root)
        
    def search(self, data, curr):
        if(curr ==  None):
            return None
        elif(curr.val == data):
            return curr
        elif(data < curr.val):
            return self.search(data, curr.left)
        else:
            return self.search(data, curr.right)