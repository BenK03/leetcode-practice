# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if ((not p) and (q)) or ((not q) and p):
            return False
        if (not p) and (not q):
            return True

        queue_p = []
        queue_p.append(p)

        queue_q = []
        queue_q.append(q)

        while queue_p and queue_q:

            node_p = queue_p.pop(0)
            node_q = queue_q.pop(0)

            if node_q.val != node_p.val:
                return False
            
            if node_p.left and node_q.left:
                queue_p.append(node_p.left)
                queue_q.append(node_q.left)
            elif node_p.left != node_q.left:
                return False

            if node_p.right and node_q.right:
                queue_p.append(node_p.right)
                queue_q.append(node_q.right)
            elif node_p.right != node_q.right:
                return False
        

        return True

    # time complexity O(n^2)