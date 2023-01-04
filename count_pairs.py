class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        for i in range(len(words) - 1):
            first_set = set(words[i])
            for j in range(i + 1, len(words)):
                second_set = set(words[j])
                if second_set == first_set:
                    count += 1
        
        return count
