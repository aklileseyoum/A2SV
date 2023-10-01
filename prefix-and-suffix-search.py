class TriNode:
    def __init__(self):
        self.children = {}
        self.EndOfWord = False

    
class WordFilter:
    def __init__(self, words: List[str]):
        self.forward = TriNode()
        self.backward = TriNode()
        self.dictionary = defaultdict(list)
        self.memo_forward = defaultdict(list)
        self.memo_backward = defaultdict(set)

        def insert(word, trie):
            dummy = trie
            for letter in word:
                if letter not in dummy.children:
                    dummy.children[letter] = TriNode()
                dummy = dummy.children[letter]
            dummy.EndOfWord = True

        for idx in range(len(words)):
            self.dictionary[words[idx]].append(idx)
            insert(words[idx], self.forward)
            insert(words[idx][::-1], self.backward)

    def f(self, pref: str, suff: str) -> int:
        def read(another, word):
            if len(another.children) == 0:
                storage.add(word)
                return

            for letter in another.children:
                if another.children[letter].EndOfWord:
                    storage.add(word + letter)
                read(another.children[letter], word + letter)

        forpref = self.forward
        Full = True
        for letter in pref:
            if letter in forpref.children:
                forpref = forpref.children[letter]
            else:
                Full = False
                break

        if self.memo_forward[pref] == []:
            storage = set()
            if Full:
                read(forpref, pref)
            if self.dictionary[pref] != []:
                storage.add(pref)
            self.memo_forward[pref] = list(storage)
        forforward = self.memo_forward[pref]

        forsuff = self.backward
        Full = True
        for idx in range(len(suff)-1, -1, -1):
            if suff[idx] in forsuff.children:
                forsuff = forsuff.children[suff[idx]]
            else:
                Full = False
                break

        if len(self.memo_backward[suff]) == 0:
            storage = set()
            if Full:
                read(forsuff, suff[::-1])
            if self.dictionary[suff] != []:
                storage.add(suff[::-1])
            self.memo_backward[suff] = storage
        
        answer = []
        for each in forforward:
            if each[::-1] in self.memo_backward[suff]:
                answer.append(each)
        
        ans = [-1]
        for each in answer:
            ans += self.dictionary[each]
        
        return max(ans)