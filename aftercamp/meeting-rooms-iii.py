class Solution(object):
    def mostBooked(self, n, meetings):
        """
        :type n: int
        :type meetings: List[List[int]]
        :rtype: int
        """
        freq = {i: 0 for i in range(n)}
        heapq.heapify(meetings)
        heap_arr = []
        nextt = 0
        full = False
        while meetings:
            start, end = heapq.heappop(meetings)
            if not heap_arr:
                heap_arr.append([end, nextt])
                freq[nextt] += 1
                nextt += 1
                if nextt == n:
                    full = True
            else:
                found = False
                selected = float('inf')
                for ending, room in heap_arr:
                    if start >= ending:
                        found = True
                        selected = min(selected, room)
                if found:
                    freq[selected] += 1
                    for idx in range(len(heap_arr)):
                        if heap_arr[idx][1] == selected:
                            heap_arr[idx][0] = end
                else:
                    if not full:
                        heap_arr.append([end, nextt])
                        freq[nextt] += 1
                        nextt += 1
                        if nextt == n:
                            full = True
                    else:
                        heapq.heapify(heap_arr)
                        ending, room = heapq.heappop(heap_arr)
                        freq[room] += 1
                        ending -= start
                        ending += end
                        heap_arr.append([ending, room])

        maxi = max(list(freq.values()))
        for k, v in freq.items():
            if v == maxi:
                return k
                