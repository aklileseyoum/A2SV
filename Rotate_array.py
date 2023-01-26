class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        idx = abs(len(nums) - k)
        if idx != 0:
            idx2 = 0
            num = nums[idx-1]
            while idx < len(nums):
                nums.insert(idx2,nums.pop(idx))
                idx += 1
                idx2 += 1

            nums[len(nums)-1] = num
