# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        D = {}
        temp = head
        while(temp):
            if(temp in D):
                return True
            D[temp] = temp.val
            temp = temp.next
        return False
        