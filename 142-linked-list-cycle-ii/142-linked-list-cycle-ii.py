# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        while(fast and fast.next):
            slow = slow.next
            fast = fast.next.next
            if(slow == fast):
                cycle_len = self.length(slow, fast)
                return self.start(head, cycle_len)
                break
        return None
    
    def start(self, head, length):
        first = second = head
        for i in range(length):
            second = second.next
        while(first != second):
            first = first.next
            second = second.next
        return first
        pass
    
    def length(self, slow, fast):
        slow = slow.next
        count = 1
        while(slow != fast):
            slow = slow.next
            count += 1
        return count