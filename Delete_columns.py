class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count = 0

        for col in range(len(strs[0])):
            first_ascii = 0

            for row in range(len(strs)):
                letter = strs[row][col]
                second_ascii = ord(letter)
                
                if first_ascii <= second_ascii:
                    first_ascii = second_ascii
                else:
                    count += 1
                    break

        return count
