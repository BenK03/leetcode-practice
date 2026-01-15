class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for i in range(len(nums)):
            target_num = target - nums[i]
            if target_num in hashmap:
                return [hashmap[target_num], i]
            else:
                hashmap[nums[i]] = i
            
        # time complexity O(n)