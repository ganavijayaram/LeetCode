# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(head.next == None):
            return head
        slow = head
        fast = head.next
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        if(fast == None):
            return slow
        return slow.next