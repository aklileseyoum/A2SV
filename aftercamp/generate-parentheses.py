class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        combinations = set()
        def backtracking(word, open, closed):
            if closed == n:
                combinations.add(word)
                return

            if open < n:
                backtracking(word+"(", open + 1, closed)
            if open > 0 and open > closed:
                backtracking(word+")", open, closed + 1)

        backtracking("", 0, 0)
        return list(combinations)

            
        