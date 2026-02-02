class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target <= nums[0]:
            return 0

        i = 0
        for num in nums:
            if target <= num:
                return i
            else:
                i += 1

        return i
    
    # time complexity O(n)