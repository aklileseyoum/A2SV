class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        size = 1
        answer = 1
        greater = False
        equals = False

        for idx in range(1, len(arr)):
            if arr[idx] > arr[idx-1]:
                if not greater or equals:
                    size += 1
                else:
                    answer = max(answer, size)
                    size = 2
                greater = True
                equals = False
            elif arr[idx] < arr[idx-1]:
                if greater or equals:
                    size += 1
                else:
                    answer = max(answer, size)
                    size = 2
                greater = False
                equals = False
            else:
                answer = max(answer, size)
                size = 1
                equals = True

        return max(answer, size)
