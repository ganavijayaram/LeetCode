# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        lst = []
        temp = head
        while(temp):
            lst.append(temp.val)
            temp = temp.next
        lst.sort()
        head = tail = None
        for i in lst:
            head, tail = self.insert(i, head, tail)
        return head
        
    def insert(self, val, head, tail):
        if(head == None):
            head = tail = ListNode(val)
            return (head, tail)
        node = ListNode(val)
        tail.next = node
        tail = node
        return (head, tail)
        
        
        