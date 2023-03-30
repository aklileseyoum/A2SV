class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        answer = bin(n)[2:]
        prev = answer[0]

        for idx in range(1, len(answer)):
            if prev == answer[idx]:
                return False
            prev = answer[idx]

        return True

    