class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        ones = {1:"One", 2:"Two", 3:"Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 0:"Zero"}
        tenth = {10:"Ten", 11:"Eleven", 12:"Twelve", 13:"Thirteen", 14:"Fourteen", 15:"Fifteen", 16:"Sixteen", 17:"Seventeen", 18:"Eighteen", 19:"Nineteen", 2:"Twenty", 3:"Thirty", 4:"Forty", 5:"Fifty", 6:"Sixty", 7:"Seventy", 8:"Eighty", 9:"Ninety"}
        number = str(num)
        block = []
        for idx in range(len(number) - 1, -1, -3):
            block.append(number[max(0, idx-2): idx + 1])

        def intoWords(num):
            if len(num) == 1 :
                return ones[int(num[0])]
            idx = 0
            while idx < len(num) and num[idx] == '0':
                idx += 1

            num = num[idx:]
            ans = ""
            if len(num) == 2:
                if num[0] == '1':
                    ans += tenth[int(num[0:])]
                else:
                    ans += tenth[int(num[0])]
                    if num[1] != '0':
                        ans += " " + ones[int(num[1])]
            elif len(num) != 0:
                ans += ones[int(num[0])]
                if len(num) == 3:
                    ans += " Hundred"
                    if num[1] == '1':
                        ans += " " + tenth[int(num[1:])]
                    else:
                        if num[1] != '0':
                            ans += " " + tenth[int(num[1])]
                        if num[2] != '0':
                            ans += " " + ones[int(num[2])]


            return ans


        ans = []
        connectors = ["Billion", "Million", "Thousand"]
        idx2 = 4 - len(block)
        for idx in range(len(block)-1, -1, -1):
            new = intoWords(block[idx])
            if new != "":
                ans.append(new)
            if idx - 1 >= 0 and new != "":
                ans.append(connectors[idx2])
                idx2 += 1

        return ' '.join(ans)
