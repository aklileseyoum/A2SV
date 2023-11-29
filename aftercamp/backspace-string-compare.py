class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_stack = []
        t_stack = []
        for letter in s:
            if letter == "#":
                if s_stack:
                    s_stack.pop()
            else:
                s_stack.append(letter)

        for letter in t:
            if letter == "#":
                if t_stack:
                    t_stack.pop()
            else:
                t_stack.append(letter)

        return (s_stack == t_stack)
        