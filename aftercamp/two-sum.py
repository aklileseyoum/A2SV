class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        visited = {}
        ans = []
        for idx in range(len(nums) - 1, -1, -1):
            val = target - nums[idx]
            if val in visited:
                ans.append(idx)
                ans.append(visited[val])
                break
            visited[nums[idx]] = idx

        return ans
        