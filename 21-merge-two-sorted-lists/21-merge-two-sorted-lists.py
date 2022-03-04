# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if(list1 == None and list2 == None):
            return None
        if(list1 == None):
            return list2
        if(list2 == None):
            return list1
        if(list1.val >= list2.val):
            start1 = list1
            start2 = list2
            y = 1
        else:
            start1 = list2
            start2 = list1
            y = 2
        prev2 = start2
        x = 0
        next1 = None
        while((start1) and (start2)):
            while((start1) and (start2) and (start1.val >= start2.val)):
                prev2 = start2
                start2 = start2.next
                x = 1
            if(x == 1):
                x = 0
                continue
            next1 = start1.next
            prev2.next = start1
            prev2 = start1
            prev2.next = start2
            start1 = next1
        while(start1):
            next1 = start1.next
            prev2.next = start1
            prev2 = start1
            start1 = next1
        if(y == 1):
            return list2
        return list1