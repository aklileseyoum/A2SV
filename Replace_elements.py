class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        store = []
        maxi = 0
        idx = len(arr) - 1
        while idx >= 0:
            saved = arr[idx]
            if idx == len(arr) - 1:
                arr[idx] = -1
            else:
                arr[idx] = maxi
            if maxi < saved:
                maxi = saved
            idx -= 1
        
        return arr
