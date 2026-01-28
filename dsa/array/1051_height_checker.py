class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        expected = sorted(heights)
        res = 0

        for i in range(len(heights)):
            if expected[i] != heights[i]:
                res = res + 1
        
        return res
    
    # time complexity O(n)