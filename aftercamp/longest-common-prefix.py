class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        def common(str1, str2):
            ans = ""
            for idx in range(min(len(str1), len(str2))):
                if str1[idx] == str2[idx]:
                    ans += str1[idx]
                else:
                    break

            return ans

        answer = strs[0]
        for idx in range(1, len(strs)):
            answer = common(answer, strs[idx])

        return answer
        