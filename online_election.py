class TopVotedCandidate:
    def __init__(self, persons: List[int], times: List[int]):
        self.persons = persons
        self.times = times
        self.count = []
        for idx in range(len(self.persons)):
            i = Counter(self.persons[:idx+1])
            self.count.append(i)
        

    def q(self, t: int) -> int:
        idx = bisect_left(self.times, t)
        if idx >= len(self.times) or self.times[idx] > t:
            idx -= 1
    
        compare = self.count[idx]
        max_value = max(list(compare.values()))
        
        while compare[self.persons[idx]] != max_value:
            idx -= 1
        
        return self.persons[idx]
        
            
        
        
        
            

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)