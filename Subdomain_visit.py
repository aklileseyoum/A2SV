class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        dictionary = {}
        answer = []
        for i in cpdomains:
            space = i.index(" ")
            number = int(i[:space])
            domain = i[space+1:]
            if domain in dictionary:
                dictionary[domain] += number
            else:
                dictionary[domain] = number
            if '.' in domain:
                index1 = domain.index(".")
                subdomain1 = domain[index1+1:]
                if subdomain1 in dictionary:
                    dictionary[subdomain1] += number
                else:
                    dictionary[subdomain1] = number
                if '.' in subdomain1:
                    index2 = subdomain1.index(".")
                    subdomain2 = subdomain1[index2+1:]
                    if subdomain2 in dictionary:
                        dictionary[subdomain2] += number
                    else:
                        dictionary[subdomain2] = number

        for key, value in dictionary.items():
            ans = str(value) + " " + key
            answer.append(ans)

        return answer
