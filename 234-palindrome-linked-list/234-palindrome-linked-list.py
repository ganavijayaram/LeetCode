# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        itr = head
        l = []
        while(itr):
            l.append(itr.val)
            itr = itr.next
        start = 0
        end = len(l) - 1
        while(start < end):
            if(l[start] != l[end]):
                return False
            start += 1
            end -= 1
        return True