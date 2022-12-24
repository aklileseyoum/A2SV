class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        arr_t = list(t)
        arr_s = list(s)
        for i in t:
            if i in arr_s:
                arr_s.remove(i)
                arr_t.remove(i)
            else:
                return i  
        if arr_t:
            return arr_t[0]
