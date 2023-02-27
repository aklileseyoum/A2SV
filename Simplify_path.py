class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ""
        dot = 0
        for idx in range(len(path)):
            if path[idx] == '/':
                if dot >= 3:
                    for i in range(dot):
                        stack += '.'
                elif dot == 2:
                    slash = 1
                    while stack and slash < 2:
                        stack = stack[:len(stack)-1]
                        if stack and stack[-1] == '/':
                            slash += 1
                dot = 0
                if not stack or (stack[-1] != '/' and idx != len(path) - 1):
                    stack += '/'
            elif path[idx] == '.':
                if stack[-1] == '/':
                    dot += 1
                else:
                    stack += '.'
            else:
                for i in range(dot):
                    stack += '.'
                stack += path[idx]
                dot = 0

        if dot == 2:
            slash = 1
            while stack and slash < 2:
                stack = stack[:len(stack)-1]
                if stack and stack[-1] == '/':
                    slash += 1
        elif dot >= 3:
            for i in range(dot):
                stack += '.'
                

        if stack and stack[-1] == '/':
            stack = stack[:len(stack)-1]

        if not stack:
            stack += '/'

        return stack
