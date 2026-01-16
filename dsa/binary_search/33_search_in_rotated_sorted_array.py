class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = 0
        h = len(nums) - 1
        
        while l <= h:
            mid = (l + h) // 2

            if target == nums[mid]:
                return mid
            
            elif nums[l] <= nums[mid]:
                # on left side
                if nums[l] <= target < nums[mid]:
                    h = mid - 1
                
                # on right side
                else:
                    l = mid + 1
            
            else: 
                # on right side
                if nums[mid] < target <= nums[h]:
                    l = mid + 1
                
                # on left side
                else:
                    h = mid - 1

        return -1
    
    # time complexity O(logn)