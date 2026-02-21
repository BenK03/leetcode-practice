class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        words = s.split()
        ans = len(words[-1])

        return ans

        # time complexity O(n)