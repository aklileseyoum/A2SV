class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        answer = []
        for index in range(len(nums)):
            if nums[index] == target:
                answer.append(index)

        return answer
