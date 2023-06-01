class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = {}
        ans = 1
        for idx in range(len(arr)-1, -1, -1):
            num = arr[idx] + difference
            if num in memo:
                memo[arr[idx]] = memo[num] + 1
                ans = max(ans, memo[arr[idx]])
            else:
                memo[arr[idx]] = 1

        return ans