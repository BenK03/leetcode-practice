# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if not root:
            return 0
        queue = []
        queue.append(root)
        count = 0

        while queue:
            node = queue.pop(0)
            count += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return count

    # time complexity O(n^2)