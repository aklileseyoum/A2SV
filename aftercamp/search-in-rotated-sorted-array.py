class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        start = nums[0]
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] >= start:
                if mid + 1 < len(nums) and nums[mid] < nums[mid + 1]:
                    left = mid + 1
                else:
                    climax = mid
                    break
            else:
                right = mid - 1

        def binarySearch(nums, target):
            left = 0
            right = len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] == target:
                    return mid
                else:
                    right = mid - 1

            return -1
        
        if target >= start and target <= nums[climax]:
            return binarySearch(nums[:climax + 1], target)
            
        if climax + 1 < len(nums) and target >= nums[climax + 1] and target <= nums[-1]:
            ans = binarySearch(nums[climax + 1:], target)
            if ans == -1:
                return ans
            return (ans + climax + 1)
        

        return -1
