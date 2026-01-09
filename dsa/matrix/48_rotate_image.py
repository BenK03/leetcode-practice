class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        while left < right and top < bottom:
            for i in range(right - left):
                top_left = matrix[top][left + i]

                # bottom left to top left
                matrix[top][left + i] = matrix[bottom - i][left]

                # bottom right to bottom left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # top right to bottom right
                matrix[bottom][right - i] = matrix[top + i][right]

                # top left to top right
                matrix[top + i][right] = top_left

            left += 1
            right -= 1
            top += 1
            bottom -= 1

    # time complexity O(n^2)