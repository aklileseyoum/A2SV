class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = 0
        sub_string = ""
        for index in range(len(s)):
            if s[index] in sub_string:
                index2 = sub_string.index(s[index])
                sub_string = sub_string[index2+1:]
                sub_string += s[index]
            else:
                sub_string += s[index]
            if answer < len(sub_string):
                answer = len(sub_string)

        return answer
