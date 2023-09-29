class TriNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = 0

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        root = TriNode()

        def insert(word):
            dummy = root
            for letter in word:
                if letter not in dummy.children:
                    dummy.children[letter] = TriNode()
                dummy = dummy.children[letter]
            dummy.EndOfWord += 1

        for word in words:
            insert(word)

        position = defaultdict(list)
        for idx in range(len(s)):
            position[s[idx]].append(idx)

        def dfs(root, idx, dictionary):
            if len(root.children) == 0:
                return

            for letter in root.children:
                if letter in dictionary or dictionary[letter] != []:
                    new = bisect_right(dictionary[letter], idx)
                    if dictionary[letter] and new < len(dictionary[letter]):
                        new_idx = dictionary[letter][new]
                        diff = new_idx - idx
                        if root.children[letter].EndOfWord:
                            ans[-1] += root.children[letter].EndOfWord
                        dfs(root.children[letter], idx + diff, dictionary)

        ans = [0]
        dfs(root, -1, position)

        return ans[-1]