class TriNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TriNode()

    def addWord(self, word: str) -> None:
        dummy = self.root
        for letter in word:
            if letter not in dummy.children:
                dummy.children[letter] = TriNode()
            dummy = dummy.children[letter]
        dummy.EndOfWord = True

    def search(self, word: str) -> bool:
        dummy = self.root

        def dfs(dummy, idx):
            if idx == len(word) - 1:
              if word[idx] == '.':
                for letter in dummy.children:
                  if dummy.children[letter].EndOfWord:
                    return True
              elif word[idx] in dummy.children and dummy.children[word[idx]].EndOfWord:
                return True
              return False
             
            if word[idx] == '.':
                ans = False
                for letter in dummy.children:
                    ans = ans or dfs(dummy.children[letter], idx + 1)
            else:
                if word[idx] not in dummy.children:
                    return False
                ans = dfs(dummy.children[word[idx]], idx+1)

            return ans

        return dfs(dummy, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
# def dfs(root, ancestor):
#     if len(root.children) == 0:
#         return 

#     for l in root.children:
#         if l < ancestor
#         dfs(root.children[l], l)