class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negs = [-i for i in stones]
        while len(negs) > 1:
            heapify(negs)
            first = -1 * heappop(negs)
            second = -1 * heappop(negs)
            heappush(negs, (second - first))

        if negs:
            return (-1 * negs[-1])

        return 0