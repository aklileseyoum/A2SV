class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for index in range(len(nums)-1):
            if nums[index] ==nums[index + 1]:
                nums[index] *= 2
                nums[index + 1] = 0
                index += 1
            index += 1

        write = 0
        read = 0

        while read < len(nums):
            if nums[read] != 0:
                temp = nums[read]
                nums[read] = nums[write]
                nums[write] = temp
                write += 1
            read += 1

        return nums
