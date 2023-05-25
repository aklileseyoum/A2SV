class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill = defaultdict(int)
        for each in bills:
            bill[each] += 1
            if each == 10:
                if bill[5] > 0:
                    bill[5] -= 1
                else:
                    return False
            elif each == 20:
                if bill[5] > 0:
                    if bill[10] > 0:
                        bill[10] -= 1
                    elif bill[5] >= 3:
                        bill[5] -= 2
                    else:
                        return False
                    bill[5] -= 1   
                else:
                    return False

        return True