# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        visited = {}

        while not(head is None): # if None break and return False
            if head in visited:
                return True
            visited[head] = True # for "if head in visited" to work you need the node as the key
            head = head.next
        return False

    # time complexity O(n)

    # Logic (hashtable):
    # Create a hashtable and start inserting the nodes into it 
    # Do not insert the value as duplicates may occur
    # If you see that same node again in the hashtable we can decect a cycle
    # As the same node can't appear twice unless there is a cycle

    # Logic (Floyd Cycle Dectection Algorithm)
    # 2 pointers. Slow and Fast.
    # Slow pointer moves at 1 per cycle e.g., slow.next
    # Fast pointer moves at 2 per cycle e.g., fast.next.next
    # If there is a cycle eventually the two pointers will intersect indicating cycle
    # If the fast pointer points to NULL there is no cycle


            

        
