# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insert(self, val):
        if(self.head == None):
            self.head = ListNode(val)
            self.tail = self.head
            #self.display(self.head)
            return self.head
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        #self.display(self.head)
        return self.head
        
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if(list1 == None):
            return list2
        if(list2 == None):
            return list1
        if(list1 == None and list2 == None):
            return list1
        while(list1 != None and list2 != None):
            if(list1.val < list2.val):
                self.insert(list1.val)
                list1 = list1.next
            else:
                self.insert(list2.val)
                list2 = list2.next
            #self.display(self.head)
        while(list1 != None):
            self.insert(list1.val)
            list1 = list1.next
        while(list2 != None):
            self.insert(list2.val)
            list2 = list2.next
        #self.display(self.head)
        return self.head
    

