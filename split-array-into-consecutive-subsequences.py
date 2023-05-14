class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        length = defaultdict(list)
        for num in nums:
            val =0
            if length[num - 1]:
                heapify(length[num - 1])
                val = heappop(length[num - 1])
            length[num].append(val + 1)

        for each in length.values():
            for v in each:
                if v < 3:
                    return False

        return True