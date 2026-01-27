# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if not head:
            return head

        dummy = ListNode(0, head)

        l = dummy
        r = head
        for _ in range(n):
            r = r.next
        
        while r:
            r = r.next
            l = l.next

        l.next = l.next.next

        return dummy.next
    
    # time complexity O(n)