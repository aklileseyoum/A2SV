class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zeros = nums.count(0)
        length = len(nums) - zeros
        i = 0
        while i < length:
            if nums[i] == 0:
                nums.remove(0)
                nums.append(0)
            else:
                i += 1
