class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        found = 0
        for i in arr:
            if i == 0:
                if arr.count(0) > 1:
                    found = 1
            else:
                if i%2 == 0:
                    j = i / 2
                    if j in arr:
                        found = 1
        
        if found == 1:
            return True
        else:
            return False
