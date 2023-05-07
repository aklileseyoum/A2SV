class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        answer = []

        subsets = []
        def backtracking(index):
            if index >= len(nums):
                ans = 0
                for each in subsets:
                    ans |= each
                answer.append(ans)
                return
            subsets.append(nums[index])
            backtracking(index + 1)
            subsets.pop()
            backtracking(index + 1)

        backtracking(0)
        maximum = max(answer)
        count = 0
        for each in answer:
            if each == maximum:
                count += 1

        return count