class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        length = len(arr)
        while i < length:
            if arr[i] == 0:
                arr.insert(i+1,0)

                i += 2
            else:
                i += 1

        new_len = len(arr)
        while new_len > length:
            arr.pop()
            new_len -= 1
