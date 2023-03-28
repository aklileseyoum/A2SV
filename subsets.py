class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = []

        subsets = []
        def backtracking(index):
            if index >= len(nums):
                answer.append(subsets[:])
                return
            subsets.append(nums[index])
            backtracking(index + 1)
            subsets.pop()
            backtracking(index + 1)

        backtracking(0)
        return answer