class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        freq = {}
        for idx in range(len(strs)):
            str_freq = Counter(strs[idx])
            str_freq = sorted(str_freq.items())
            key = ""
            for k, v in str_freq:
                key += str(k)
                key += str(v)
            if key not in freq:
                freq[key] = []
            freq[key].append(idx)
        
        ans = []
        for k, v in freq.items():
            each = []
            for idx in v:
                each.append(strs[idx])
            ans.append(each)

        return ans

        