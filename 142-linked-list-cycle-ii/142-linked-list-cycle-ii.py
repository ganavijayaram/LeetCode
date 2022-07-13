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
        temp = head
        counter = 0
        D = {}
        while(temp):
            if(temp in D):
                return temp
            D[temp] = counter
            counter += 1
            temp = temp.next
        return None