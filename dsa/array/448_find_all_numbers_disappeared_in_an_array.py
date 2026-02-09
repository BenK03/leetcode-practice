class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        numbers = set(nums)

        for i in range(1, len(nums) + 1):
            if i not in numbers:
                ans.append(i)

        return ans
            
    # time complexity O(n)