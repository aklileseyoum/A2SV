class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for i in range(len(nums1) + 1)] for j in range(len(nums2) + 1)]
        
        for row in range(len(nums2)-1, -1, -1):
            for col in range(len(nums1)-1, -1, -1):
                if nums2[row] == nums1[col]:
                    dp[row][col] = 1 + dp[row+1][col+1]
                else:
                    dp[row][col] = max(dp[row+1][col], dp[row][col+1])

        return dp[0][0]