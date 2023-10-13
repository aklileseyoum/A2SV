class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        def isIPv6(ip):
            nums = ip.split(":")

            if len(nums) != 8:
                return False

            for num in nums:
                if len(num) > 4 or len(num) < 1:
                    return False

                for each in num:
                    if not each.isnumeric():
                        if  not((ord(each) >= 65 and ord(each) <= 70) or (ord(each) >= 97 and ord(each) <= 102)):
                            return False

            return True

        def isIPv4(ip):
            nums = ip.split('.')
            if len(nums) != 4:
                return False
            
            for num in nums:
                if num == "" or (len(num) > 1 and num[0] == '0'):
                    return False
                    
                if not num.isnumeric():
                    return False

                if int(num) > 255:
                    return False

            return True

        double_dots = queryIP.count(':')
        if double_dots:
            if isIPv6(queryIP):
                return "IPv6"
        else:
            if isIPv4(queryIP):
                return "IPv4"
           
        return "Neither"