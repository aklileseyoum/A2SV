class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for sign in s:
            if sign == '(':
                stack.append(sign)
            else:
                if stack[-1] != '(':
                    num = stack.pop()
                    stack.pop()
                    num *= 2
                else:
                    stack.pop()
                    num = 1
                if stack and stack[-1] != '(':
                    num += stack.pop() 
                stack.append(num)

        return stack.pop()