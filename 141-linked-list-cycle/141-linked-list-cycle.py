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
        slow = fast = head
        if(fast == None):
            return False
        if(fast.next != None):
            fast = fast.next
            slow = slow.next
        else:
            return False
        if(fast.next != None):
            fast = fast.next
        else:
            return False
        while(fast != None):
            if(slow == fast):
                return True
            slow = slow.next
            fast = fast.next
            if(fast != None):
                fast = fast.next
        return False
        
        