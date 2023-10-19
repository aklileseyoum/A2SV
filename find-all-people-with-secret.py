class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        graph = {i: i for i in range(n)}
        graph[firstPerson] = 0
        meetings.sort(key=lambda x: x[2])
        
        def union(x, y):
            xrep = find(x)
            yrep = find(y)
            if xrep != yrep:
                if xrep == 0:
                    graph[yrep] = xrep
                elif yrep == 0:
                    graph[xrep] = yrep
                else:
                    if xrep > yrep:
                        graph[xrep] = yrep
                    else:
                        graph[yrep] = xrep

        def find(x):
            if x == graph[x]:
                return x
            graph[x] = find(graph[x])
            return graph[x]
        
        ans = [0, firstPerson]
        time = meetings[0][2]
        store = set()
        for idx in range(len(meetings)): 
            union(meetings[idx][0], meetings[idx][1])
            
            store.add(meetings[idx][0])
            store.add(meetings[idx][1])

            if idx + 1 < len(meetings) and time != meetings[idx + 1][2]:
                for each in store:
                    if find(each) ==  0:
                        ans.append(each)
                    else:
                        graph[each] = each
                time = meetings[idx + 1][2]
                store = set()

        for each in store:
            if find(each) == 0:
                ans.append(each)
            
        
        return list(set(ans))