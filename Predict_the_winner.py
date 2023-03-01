class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def play(start, end, turn):
            if start == end:
                if turn:
                    return ([nums[start], 0])
                return ([0, nums[start]])

            first = play(start + 1, end, not turn)
            last = play(start, end - 1, not turn)

            if turn:
                on_start = first[0] + nums[start]
                on_end = last[0] + nums[end]
                if on_start > on_end:
                    first[0] += nums[start]
                    return first
                else:
                    last[0] += nums[end]
                    return last

            on_start = first[1] + nums[start]
            on_end = last[1] + nums[end]
            
            if on_start > on_end:
                first[1] += nums[start]
                return first
            else:
                last[1] += nums[end]
                return last

        scores = play(0, len(nums)-1, True)
        if scores[0] >= scores[1]:
            return True
        return False
        