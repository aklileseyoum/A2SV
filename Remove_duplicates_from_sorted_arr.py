class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        pt1 = 0
        pt2 = 1
        last_max = -101
        swaps = 1
        while pt1 < len(nums) and pt2 < len(nums):
            if nums[pt1] > nums[pt2]:
                if nums[pt1] > last_max:
                    last_max = nums[pt1]
                    nums[pt1], nums[pt2] = nums[pt2], nums[pt1]
                    pt2 += 1
                    swaps += 1
            elif nums[pt1] < nums[pt2]:
                pt2 += 1
                swaps += 1
            pt1 += 1

        nums[pt2:] = '_'
        
        return swaps
