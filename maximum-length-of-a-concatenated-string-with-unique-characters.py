class Solution:
    def maxLength(self, arr: List[str]) -> int:
        ans = [0]
        subsets = []
        def backtracking(idx):
            if idx >= len(arr):
                sentence = ""
                yes = True
                for each in subsets:
                    container = set()
                    for letter in each:
                        container.add(letter)
                        if letter in sentence:
                            yes = False
                    if len(container) != len(each):
                        yes = False
                    sentence += each
                    
                if (yes):
                    ans[0] = max(len(sentence), ans[0])
                return
            subsets.append(arr[idx])
            backtracking(idx + 1)
            subsets.pop()
            backtracking(idx + 1)

        backtracking(0)
        return ans[-1]