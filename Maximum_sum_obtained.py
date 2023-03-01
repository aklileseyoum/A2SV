class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        prefix_sum = [0] * len(nums)

        for request in requests:
            prefix_sum[request[0]] += 1
            if request[1] + 1 < len(nums):
                prefix_sum[request[1] + 1] -= 1

        prev = 0
        for idx in range(len(prefix_sum)):
            prefix_sum[idx] += prev
            prev = prefix_sum[idx]

        prefix_sum.sort(reverse = True)
        nums.sort(reverse=True)
        print(prefix_sum)
        answer = 0
        for idx in range(len(prefix_sum)):
            if prefix_sum[idx] == 0:
                break
            answer += prefix_sum[idx] * nums[idx]

        return answer % (10**9 + 7)