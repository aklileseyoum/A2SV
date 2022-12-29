class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = 0
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(val)
                nums.append('_')
                result += 1
            else:
                i += 1
            

        result = len(nums) - result

        return result
