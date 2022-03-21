# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        curr = root
        total = 0
        stack = []
        while(curr or len(stack)):
            while(curr):
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            if(curr and (curr.val >= low and curr.val <= high)):
                    total += curr.val
            curr = curr.right
        return total
                