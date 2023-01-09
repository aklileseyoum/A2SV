class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        answer = []
        space = set(spaces)
        for index, character in enumerate(s):
            if index in space:
                answer.append(" ")
            answer.append(character)

        return "".join(answer)
