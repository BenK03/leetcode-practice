class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hashmap = {}

        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1

        max_value = 0
        ans = None
        for key in hashmap:
            if hashmap[key] >= max_value:
                max_value = hashmap[key]
                ans = key

        return ans

    # time complexity O(n)