class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        first = 0
        last = len(people) - 1
        people.sort()
        boats = 0

        while first < last:
            if people[last] == limit or people[last] + people[first] > limit:
                boats += 1
                last -= 1
            elif people[last] + people[first] <= limit:
                boats += 1
                last -= 1
                first += 1
        if first == last:
            boats += 1
        return boats    
