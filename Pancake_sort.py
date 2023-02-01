class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(index):
            left = 0
            right = index
            while left < right:
                arr[left], arr[right] = arr[right], arr[left]
                left += 1
                right -=1
            return arr

        n = len(arr) - 1
        
        answer = []

        while n > 0:
            maxi = max(arr[:n+1])
            idx = arr.index(maxi)
            if idx == 0:
                flip(n)
                answer.append(n+1)
                n -= 1
                continue
            flip(idx)
            flip(n)
            answer.append(idx+1)
            answer.append(n+1)
            n -= 1
            

        return answer
        
