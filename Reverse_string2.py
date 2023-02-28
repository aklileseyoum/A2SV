class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        idx1 = 0
        idx2 = len(s) - 1

        def rev(idx1, idx2):
            if idx1 >= idx2:
                return 0
            s[idx1], s[idx2] = s[idx2], s[idx1]
            idx1 += 1
            idx2 -= 1
            rev(idx1, idx2)

        
        return rev(idx1, idx2)
