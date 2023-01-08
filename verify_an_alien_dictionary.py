class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        i  = 0
        j = 0
        false = 0
        while i + 1 < len(words):
            if j >= len(words[i]) and j >= len(words[i+1]):
                i += 1
                j = 0
                continue
            elif j >= len(words[i]):
                position1 = -1
                char2 = words[i+1][j]
                position2 = order.index(char2)
            elif j >= len(words[i+1]) and j < len(words[i]):
                position2 = -1
                char1 = words[i][j]
                position1 = order.index(char1)
            elif i < len(words) and j < len(words[i+1]):
                char1 = words[i][j]
                position1 = order.index(char1)
                char2 = words[i+1][j]
                position2 = order.index(char2)
            
            if position1 > position2:
                false = 1
                break
            elif position1 == position2:
                j += 1
                i -= 1
            i += 1

        if false == 0:
            return True
        else:
            return False
