class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pt1 = 0
        pt2 = 1
        while pt2 < len(nums):
            if nums[pt1] == nums[pt2]:
                pt2 += 1
            else:
                pt1 += 1
                nums[pt1], nums[pt2] = nums[pt2], nums[pt1]
                pt2 += 1

        return pt1 + 1
        
        