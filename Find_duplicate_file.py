class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        from collections import defaultdict
        new = []
        saved =  ""
        dictionary = defaultdict(list)
        file = ""
        
        for path in paths:
            path_arr = list(path.split(" "))
            directory = path_arr[0]
            j = len(path_arr) - 1
            while j > 0:
                current = path_arr[j]
                if '(' in current:
                    index1 = current.index('(')
                    index2 = current.index(')')
                    saved = current[index1 + 1:index2]
                    file = directory + "/" + current[:index1]
                    dictionary[saved].append(file)
                j -= 1

        k = 0
        for key,value in dictionary.items():
            if len(value) >= 2:
                k += 1
        answer = [[]] * k
        i = 0
        for key,value in dictionary.items():
            if len(value) >= 2:
                answer[i] = list(value)
                i += 1

       
        return answer
