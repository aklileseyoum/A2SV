class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        prefix_sum = []
        prev = 0
        for num in nums:
            prefix_sum.append(prev + num)
            prev += num

        seen = defaultdict(int)
        answer = 0
        for num in prefix_sum:
            if num == k:
                answer += 1
            
            diff = num - k
            answer += seen[diff]
            seen[num] += 1

        return answer
