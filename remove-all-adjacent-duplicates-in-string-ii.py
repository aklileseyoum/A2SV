class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        
        for letter in s:
            if stack and stack[-1][0] == letter:
                if stack[-1][1] == k - 1:
                    stack.pop()
                else:
                    stack[-1][1] += 1
            else:
                stack.append([letter, 1])

        ans = ""
        for letter, count in stack:
            ans += letter * count

        return ans