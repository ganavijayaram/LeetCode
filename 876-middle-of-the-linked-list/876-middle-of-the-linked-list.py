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
        temp = head
        D = {}
        count = 1
        while(temp):
            D[count] = temp
            count += 1
            temp = temp.next
        count -= 1
        return D[count//2 + 1]