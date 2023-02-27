class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        max_len = 0
        for trip in trips:
            max_len = max(trip[-1], max_len)

        travel = [0 for _ in range(max_len + 1)]
        for trip in trips:
            travel[trip[1]] += trip[0]
            travel[trip[2]] -= trip[0]

        prev = 0
        for idx in range(len(travel)):
            travel[idx] += prev
            prev = travel[idx]
        
        for i in travel:
            if i > capacity:
                return False

        return True
