class Solution:
    def findComplement(self, num: int) -> int:
        bit = bin(num)

        for i in range(len(bit) - 2):
            num ^= (1 << i)

        return num