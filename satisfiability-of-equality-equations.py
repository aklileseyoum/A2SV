class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        graph = {}
        rank = {}
        for i in range(97, 123):
            letter = chr(i)
            graph[letter] = letter
            rank[letter] = 1

        def find(x):
            if x == graph[x]:
                return x
            graph[x] = find(graph[x])
            return graph[x]

        def union(s, d):
            srep = find(s)
            drep = find(d)
            if srep != drep:
                if rank[s] >= rank[d]:
                    graph[drep] = srep
                    rank[s] += rank[d]
                else:
                    graph[srep] = drep
                    rank[d] += rank[s]
        
        
        notEqual = []
        for equation in equations:
            if equation[1] == '!':
                notEqual.append(equation)
            else:
                union(equation[0], equation[3])
        
        for each in notEqual:
            if find(each[0]) == find(each[3]):
                return False

        return True