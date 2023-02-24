class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        ascii_val = []
        for character  in s:
            ascii_val.append(ord(character))

        change = [0] * len(s)
        for shift in shifts:
            start = shift[0]
            end = shift[1]
            direction = shift[2]
            if direction == 0:
                change[start] -= 1
                if end + 1 < len(change):
                    change[end + 1] += 1
            else:
                change[start] += 1
                if end + 1 < len(change):
                    change[end + 1] -= 1
            
        prev = 0
        for idx in range(len(change)):
            change[idx] += prev
            prev = change[idx]

        answer = []
        for idx in range(len(s)):
            answer+=chr(((ord(s[idx]) - 97 + change[idx]) % 26) +97)
        
        return ''.join(answer)
