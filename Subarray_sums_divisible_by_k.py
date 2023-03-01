class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        total = 0
        answer = 0

        for num in nums:
            total += num

            if prefix_sum[total % k]:
                answer += prefix_sum[total % k]
            

            prefix_sum[total % k] += 1

        return answer