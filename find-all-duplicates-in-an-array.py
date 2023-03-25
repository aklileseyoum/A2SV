class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        bucket = [[] for _ in range(len(nums))]
        for num in nums:
            bucket[num - 1].append(num)

        answer = []
        for each in bucket:
            if len(each) > 1:
                answer.append(each[0])

        return answer