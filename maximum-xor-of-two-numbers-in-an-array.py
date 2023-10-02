class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        bin_string = []
        max_len = 0
        for num in nums:
            bin_string.append(bin(num))
            max_len = max(max_len, len(bin(num)))

        root = {}
        def insert(word):
            dummy = root
            for letter in word:
                if letter not in dummy.keys():
                    dummy[letter] = {}
                dummy = dummy[letter]
        
        for each in bin_string:
            if len(each) == max_len:
                insert(each[2:])
            else:
                new = each[2:]
                diff = max_len - 2 - len(new)
                added = ""
                for _ in range(diff):
                    added += "0"
                new = added + new
                insert(new)
       
        def read(another, word):
            if len(another) == 0:
                self.ans.add(word)
                return

            for letter in another.keys():
                read(another[letter], word + letter)

        
        def dfs(big, normal, word1, word2, count):
            if len(big) == 0 or len(normal) == 0:
                if word1 != "":
                    num1 = int("0b"+word1, 2)
                if word2 != "":
                    num2 = int("0b"+word2, 2)
                if word1 and word2:
                    max_ans[-1] = max(max_ans[-1], (num1 ^ num2))
                return

            if len(big) == 2:
                if len(normal) == 2:
                    dfs(big['0'], normal['1'], word1+"0", word2+"1", count+1)
                    dfs(big['1'], normal['0'], word1+"1", word2+"0", count+1)
                else:
                    for second in normal.keys():
                        if second == "0":
                            dfs(big['1'], normal['0'], word1+"1", word2+"0", count+1)
                        else:
                            dfs(big['0'], normal['1'], word1+"0", word2+"1", count+1)
            else:
                if len(normal) == 2:
                    for first in big.keys():
                        if first == "0":
                            dfs(big['0'], normal['1'], word1+"0", word2+"1", count+1)
                        elif first == "1":
                            dfs(big['1'], normal['0'], word1+"1", word2+"0", count+1)
                else:
                    for (first, second) in zip(big.keys(), normal.keys()):
                        if first != second:
                            dfs(big[first], normal[second], word1+first, word2+second, count+1)
                        else:
                            self.ans = set()
                            read(big[first], word1+first)
                            first_ans = []
                            for each in self.ans:
                                first_ans.append(each)
                            
                            self.ans = set()
                            read(normal[second], word2+second)
                            second_ans = []
                            for each in self.ans:
                                second_ans.append(each)
                            
                            for val in first_ans:
                                for v in second_ans:
                                    if val != "":
                                        num1 = int("0b"+val, 2)
                                    if v != "":
                                        num2 = int("0b"+v, 2)
                                    if val and v:
                                        max_ans[-1] = max(max_ans[-1], (num1 ^ num2))
                            


        max_ans =[0]
        dummy = root
        while len(dummy) == 1:
            for letter in dummy.keys():
                dummy = dummy[letter]
        
        if len(dummy) == 2:
            dfs(dummy['1'], dummy['0'], "1", "0", 1)

        return max_ans[-1]