class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pos = [[] for _ in range(10001)]
        negs = [[] for _ in range(10001)]

        for num in nums:
            if num >= 0:
                pos[num].append(num)
            else:
                negs[num].append(num)

        sorted_nums = []
        for neg in negs:
            if len(neg) > 0:
                sorted_nums += neg

        for positive in pos:
            if len(positive) > 0:
                sorted_nums += positive
        
        idx = -1 * k
        return sorted_nums[idx]
