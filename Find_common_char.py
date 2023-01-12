class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        first = [0] * 26
        second = [0] * 26
        offset = ord('a')
        first_letter = 1
        for word in words:
            for letter in word:
                index = ord(letter) - offset
                first[index] += 1
            if first_letter == 1:
                second = first
                first_letter = 0
            else:
                for i in range(26):
                    if first[i] < second[i]:
                        second[i] = first[i]
            first = [0] * 26
        
        answer = []
        for i in range(len(second)):
            if second[i] > 0:
                for j in range(second[i]):
                    letter = chr(i+offset)
                    answer.append(letter)

        return answer
