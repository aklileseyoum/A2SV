class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p, s in zip(position, speed)]
        pair.sort()
        stack = []

        for position, speed in pair:
            time = (target - position) / speed
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)

        return len(stack)