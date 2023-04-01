class Solution:
    def maxProduct(self, words: List[str]) -> int:
        data = [0] * len(words)
        answer = 0

        for idx, word in enumerate(words):
            for letter in word:
                data[idx] |= (1 << (ord(letter) - ord('a')))

        for i in range(len(data)):
            for j in range(len(data)):
                if data[i] & data[j] == 0:
                    answer = max(answer, len(words[i]) * len(words[j]))

        return answer