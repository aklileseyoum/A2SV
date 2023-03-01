class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        last_index = defaultdict(int)
        seen = set()

        for idx in range(len(s)):
            last_index[s[idx]] = idx

        for idx in range(len(s)):
            if s[idx] not in stack:
                while stack and ord(stack[-1]) > ord(s[idx]) and last_index[stack[-1]] > idx:
                    print(last_index[stack[-1]])
                    print(idx)
                    print(last_index[stack[-1]] > idx)
                    stack.pop()
                stack.append(s[idx])
            seen.add(s[idx])

        return ''.join(stack)