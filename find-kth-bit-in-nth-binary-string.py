class Solution:
    def findKthBit(self, n: int, k: int) -> str:

        def invert(binary_string):
            new_string = []
            for idx in range(len(binary_string)-1, -1, -1):
                if binary_string[idx] == "0":
                    new_string.append("1")
                else:
                    new_string.append("0")
            return new_string

        def BinaryString(n):
            if n == 1:
                return ["0"]

            left = BinaryString(n - 1)
            answer = left + ["1"] + invert(left)
            return answer

        answer = BinaryString(n)

        return answer[k - 1]