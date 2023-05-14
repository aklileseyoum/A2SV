class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        negs = [-i for i in piles]
        heapify(negs)
        while k > 0:
            val = -1 * heappop(negs)
            val -= val // 2
            heappush(negs, -val)
            k -= 1

        answer = 0
        for each in negs:
            answer += -each

        return answer