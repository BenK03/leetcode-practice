class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = {}

        for num in nums:
            if num not in seen:
                seen[num] = "visited"
            else:
                return True
        
        return False

    # time complexity O(n)