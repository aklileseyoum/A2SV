class TriNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        dictionary = defaultdict(int)
        memo = defaultdict(list)
        root = TriNode()

        def insert(word):
            dummy = root
            for letter in word:
                if letter not in dummy.children:
                    dummy.children[letter] = TriNode()
                dummy = dummy.children[letter]
            dummy.EndOfWord = True

        def read(another, word):
            if len(another.children) == 0:
                storage.add(word)
                return
            
            for letter in another.children:
                if another.children[letter].EndOfWord:
                    storage.add(word + letter)
                read(another.children[letter], word + letter)

        for word in words:
            insert(word)
            dictionary[word] += 1
        
        answer = []
        for word in words:
            dummy = root
            letter = word[0]
            dummy = dummy.children[letter]
            if memo[letter] == []:
                storage = set()
                if dictionary[letter] != 0:
                    storage.add(letter)
                read(dummy, letter)
                memo[letter] += list(storage)
            ans = 0
            for each in memo[letter]:
                if each == word:
                    ans += dictionary[word] * (len(word))
                else:
                    idx = 0
                    while idx < len(word) and idx < len(each):
                        if each[idx] != word[idx]:
                            break
                        idx += 1
                    ans += dictionary[each] * idx

            answer.append(ans)
        
        return answer