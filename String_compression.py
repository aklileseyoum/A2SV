class Solution:
    def compress(self, chars: List[str]) -> int:
        arr = []
        pt1 = 0
        count = 1
        while pt1 < len(chars)-1:
            if chars[pt1] == chars[pt1 + 1]:
                count += 1
            else:
                arr.append(str(chars[pt1]))
                if count > 1:
                    arr.append(str(count))
                    count = 1
            pt1 += 1

        arr.append(str(chars[-1]))
        if count > 1:
            arr.append(str(count))
        
        answer = "".join(arr)

        for i in range(len(answer)):
            chars[i] = answer[i]

        return len(answer)
