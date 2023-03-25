class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        bucket = [[] for _ in range(len(nums))]
        for num in nums:
            bucket[num - 1].append(num)

        for each in bucket:
            if len(each) > 1:
                return each[0]