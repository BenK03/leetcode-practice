class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        best = 0

        while l < r:
            width = r - l
            if height[l] < height[r]:
                h = height[l]
            else:
                h = height[r]

            area = h * width
            if area > best:
                best = area

            # Move the shorter side inward
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                # Equal heights
                r -= 1

        return best
    
    # time complexity O(n)