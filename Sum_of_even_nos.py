class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        answer = []
        evens = 0
        for i in nums:
            if i % 2 == 0:
                evens += i
        
        for query in queries:
            even = 0
            if nums[query[1]] % 2 == 0:
                even = nums[query[1]]
            nums[query[1]] += query[0]
            if nums[query[1]] % 2 == 0:
                difference = nums[query[1]] - even
                evens += difference
            else:
                evens -= even
            answer.append(evens)

        return answer
