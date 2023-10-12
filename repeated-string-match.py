class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        lps = [0] * len(b)
        prev, i = 0, 1
        
        while i < len(b):
            if b[prev] == b[i]:
                lps[i] = prev + 1
                prev += 1
                i += 1
            else:
                if prev == 0:
                    i += 1
                else:
                    prev = lps[prev - 1]

        def finder(new, b):
            j = 0
            i = 0
            count = 0
            while j < len(b):
                if i == len(new):
                    count += 1
                    i = 0
                if new[i] == b[j]:
                    j += 1
                    i += 1
                else:
                    if count >= 2:
                        return -1
                    if j != 0:
                        j = lps[j - 1]
                    else:
                        i += 1

            return count+1

        return finder(a, b)