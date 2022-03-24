# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        curr = root
        a = []
        stack = []
        while(curr or len(stack)):
            if(curr):
                a.append(curr.val)
                stack.append(curr)
            else:
                curr = stack.pop()
                curr = curr.right
                continue
            if(curr and curr.left != None):
                curr = curr.left
            elif(len(stack)):
                curr = stack.pop()
                curr = curr.right
        return a
                