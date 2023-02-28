class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix_sum = []
        for num in nums:
            prefix_sum.append(num % 2)
        
        prev = 0
        for idx in range(len(prefix_sum)):
            prefix_sum[idx] += prev
            prev = prefix_sum[idx]
        
        seen = defaultdict(int)
        answer = 0
        for num in prefix_sum:
            if num < k:
                seen[num] += 1
            elif num == k:
                answer += 1
                seen[num] += 1
                if 0 in seen:
                    answer += seen[0]
            else:
                seen[num] += 1
                diff = num - k
                if diff in seen:
                    answer += seen[diff]

        return answer
