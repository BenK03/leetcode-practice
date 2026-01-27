# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        if head == None:
            return True
        if head.next == None:
            return True

        curr = head

        holder = []

        while curr is not None:
            holder.append(curr.val)
            curr = curr.next

        holder_r = holder[::-1]

        if holder_r == holder:
            return True

        return False
    
    # time complexity O(n)

