class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for sign in s:
            if sign == '(' or sign == '[' or sign == '{':
                stack.append(sign)
            elif sign == ')':
                if not stack or stack[-1] != '(':
                    return False
                stack.pop()
            elif sign == ']':
                if not stack or stack[-1] != '[':
                    return False
                stack.pop()
            elif sign == '}':
                if not stack or stack[-1] != '{':
                    return False
                stack.pop() 

        if len(stack) == 0:
            return True