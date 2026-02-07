class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seq_ones = []
        max_ = 0

        for num in nums:
            if num == 0:
                seq_ones.append(max_)
                max_ = 0
            else: 
                max_ += 1

        seq_ones.append(max_)

        return max(seq_ones)

        # time complexity O(n)