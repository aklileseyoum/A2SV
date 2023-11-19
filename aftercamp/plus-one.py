class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        def adder(idx, digits):
            if idx < 0:
                digits.insert(0, 1)
                return

            if digits[idx] == 9:
                digits[idx] = 0
                adder(idx - 1, digits)
            else:
                digits[idx] += 1

        adder(len(digits) - 1, digits)
        return digits
        