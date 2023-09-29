class TriNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False

class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TriNode()

        def insert(word):
            dummy = root
            for letter in word:
                if letter not in dummy.children:
                    dummy.children[letter] = TriNode()
                dummy = dummy.children[letter]
            dummy.EndOfWord = True
        
        for word in words:
            insert(word)

        ans = TriNode()
        answer = []
        def dfs(new, dummy):
            if len(new.children) == 0:
                return

            for letter in new.children:
                if new.children[letter].EndOfWord:
                    dummy.children[letter] = TriNode()
                    dfs(new.children[letter], dummy.children[letter])
        dfs(root, ans)
        
        max_len = [0]
        def read(another, word):
            if len(another.children) == 0:
                answer.append(word)
                max_len[-1] = max(max_len[-1], len(word))
                return

            for letter in another.children:
                read(another.children[letter], word + letter)

        read(ans, "")
        ans = []
        for word in answer:
            if len(word) == max_len[-1]:
                ans.append(word)
        ans.sort()
        return ans[0]