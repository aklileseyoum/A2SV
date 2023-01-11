class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer = []
        sub_string = ""
        for index in range(len(s)):
            if s[index] in sub_string:
                index2 = sub_string.index(s[index])
                sub_string = sub_string[index2+1:]
                sub_string += s[index]
            else:
                sub_string += s[index]
            answer.append(len(sub_string))

        if len(answer) == 0:
            result = 0
        else:
            result = max(answer)
        return result
