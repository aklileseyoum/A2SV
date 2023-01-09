class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        dictionary = collections.Counter()
        MOD = 10 ** 9 + 7

        count = 0
        for meal in deliciousness:
            for power in range(22):
                target = (1 << power) - meal
                
                if target in dictionary:
                    count += dictionary[target]
            dictionary[meal] += 1

        return count%MOD
