class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        jump_len = 0
        
        for i in range(len(nums)):
            if i > jump_len:
                return False
            if i + nums[i] > jump_len:
                jump_len = i + nums[i]
        
        return True

    # time complexity O(n)