class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(matrix) - 1

        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target <= matrix[mid][len(matrix[mid]) - 1]:
                return self.binarySearch(matrix[mid], target)
            
            elif target < matrix[mid][0]:
                right = mid - 1
            
            else:
                left = mid + 1
        
        return False

    def binarySearch(self, m, target):
        left = 0
        right = len(m) - 1

        while left <= right:
            mid = (left + right) // 2
            if m[mid] == target:
                return True
            
            elif target < m[mid]:
                right = mid - 1
            
            else:
                left = mid + 1
        
        return False
    
    # time complexity O(logm + logn)
    