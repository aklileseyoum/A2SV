class Solution(object):
    def findOriginalArray(self, changed):
        """
        :type changed: List[int]
        :rtype: List[int]
        """
        double = {}
        for each in changed:
            double[each * 2] = each

        original = []
        save = Counter(changed)
        visited = []
        changed.sort()
        for idx in range(len(changed) - 1, -1, -1):
            if changed[idx] in double and save[changed[idx]] > 0:
                original.append(double[changed[idx]])
                save[double[changed[idx]]] -= 1
                save[changed[idx]] -= 1
                visited.append(changed[idx])
                visited.append(double[changed[idx]])
            if len(original) == (len(changed) / 2):
                break
        
        visited.sort()
        if visited != changed:
            return []
            
        return original
        