class Solution:
    def arrangeCoins(self, n: int) -> int:
        def adder(num):
            return ((num * (num + 1)) // 2)

        for num in range(1, n + 1):
            if adder(num) > n:
                return num - 1

        return n