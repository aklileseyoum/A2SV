class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        array = []

        if c == 0 or c == 1:
            return True
        root = int(math.sqrt(c))
        print(root)
        for idx in range(root+1):
            array.append(idx)

        first = 0
        last = len(array) - 1

        while first < last:
            if array[first] ** 2 + array[last] ** 2 == c:
                return True
            if 2 * (array[first] ** 2) == c or 2 * (array[last] ** 2) == c:
                return True
            if array[first] ** 2 + array[last] ** 2 > c:
                last -= 1
            else:
                first += 1

        return False
