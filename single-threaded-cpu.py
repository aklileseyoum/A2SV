class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for idx in range(len(tasks)):
            tasks[idx].append(idx)

        tasks.sort(key = lambda t : t[0])
        time = tasks[0][0]
        idx = 0
        queue = []
        heapify(queue)
        answer = []
        
        while queue or idx < len(tasks):
            while idx < len(tasks) and time >= tasks[idx][0]:
                heappush(queue, (tasks[idx][1], tasks[idx][2]))
                idx += 1
            if not queue:
                time = tasks[idx][0]
            else:
                t, i = heappop(queue)
                time += t
                answer.append(i)
            
        return answer