class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        no = 0
        for i in range(len(arr) - 1):
            if arr[i] == arr[i+1]:
                no = 1
        if no == 0:
            down = 0
            up = 0
            for i in range(len(arr)-1):
                if down == 1:
                    if arr[i] < arr[i+1]:
                        return False
                else:
                    if arr[i] > arr[i+1]:
                        down = 1
                    else:
                        up = 1
            if down == 0 or up == 0:
                return False
            return True
        else:
            return False
