# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        visited = {}

        while (headA is not None) or (headB is not None):
            if headA is not None:
                if headA in visited:
                    return headA
                visited[headA] = True
                headA = headA.next


            if headB is not None:
                if headB in visited:
                    return headB
                visited[headB] = True
                headB = headB.next

        return None
    
    # time complexity O(n + m)