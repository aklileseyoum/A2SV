class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1

        diff = []
        for g, c in zip(gas, cost):
            diff.append(g-c)

        start = 0
        idx = 0
        total = 0
        while idx < len(diff):
            total += diff[idx]
            if total < 0:
                start = idx + 1
                total = 0
            idx += 1
        
        if total >= 0:
            return start