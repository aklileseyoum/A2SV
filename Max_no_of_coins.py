class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        steps = len(piles) // 3
        piles.sort()
        answer = 0
        idx = -2
        for step in range(steps):
            answer += piles[idx]
            idx -= 2

        return answer
