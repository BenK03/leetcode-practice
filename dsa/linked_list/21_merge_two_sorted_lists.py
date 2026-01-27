# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        res = ListNode()
        tail = res # tail pointer to not overwrite res

        curr1 = list1
        curr2 = list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                tail.next = curr1
                curr1 = curr1.next 
            else:
                tail.next = curr2
                curr2 = curr2.next
            
            tail = tail.next

        if curr1 and not curr2:
            tail.next = curr1
        elif curr2 and not curr1:
            tail.next = curr2
        
        return res.next
    
    # time complexity O(n + m)


        