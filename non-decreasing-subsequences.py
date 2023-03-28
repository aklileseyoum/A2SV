class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        answer = []

        subsets = []
        def backtracking(index):
            if index >= len(nums):
                boolean = True
                for idx in range(1, len(subsets)):
                    if subsets[idx - 1] > subsets[idx]:
                        boolean = False
                if boolean and len(subsets) >= 2 and subsets not in answer:
                    answer.append(subsets[:])
                return
            subsets.append(nums[index])
            backtracking(index + 1)
            subsets.pop()
            backtracking(index + 1)

        backtracking(0)
        return answer