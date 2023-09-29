class TriNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False

    
class MapSum:
    def __init__(self):
        self.storage = {}
        self.root = TriNode()

    def insert(self, key: str, val: int) -> None:
        self.storage[key] = val
        def insertNode(word):
            dummy = self.root
            for letter in word:
                if letter not in dummy.children:
                    dummy.children[letter] = TriNode()
                dummy = dummy.children[letter]
            dummy.EndOfWord = True
        insertNode(key)

    def sum(self, prefix: str) -> int:
        dummy = self.root
        answer = set()
        for letter in prefix:
            if letter in dummy.children:
                dummy = dummy.children[letter]
            else: 
                return 0

        def read(another, word):
            if len(another.children) == 0:
                answer.add(word)
                return

            for letter in another.children:
                if another.children[letter].EndOfWord:
                    answer.add(word + letter)
                read(another.children[letter], word + letter)
        
        read(dummy, "")
        ans = 0
        
        if "" in answer and len(answer) == 1:
            ans -= self.storage[prefix]
        for each in answer:
            key = prefix + each
            ans += self.storage[key]
        
        if prefix in self.storage:
            ans += self.storage[prefix]

        return ans
        


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)